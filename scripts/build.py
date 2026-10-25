#!/usr/bin/env python3
"""Build the open dataset from upstream/visa.json (China Easy Mode's source of truth).

Writes data/china-visa-free.json, data/china-visa-free.csv, datapackage.json and
README.md, and prepends an entry to CHANGELOG.md whenever the country data changes.

Usage:
  python3 scripts/build.py                 # rebuild everything
  python3 scripts/build.py --check         # exit 1 if generated files are stale
  SOURCE_COMMIT=<sha> python3 scripts/build.py   # record the upstream commit in the changelog

Standard library only, so it runs anywhere Python 3.9+ is available.
"""
import csv
import datetime as dt
import io
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "upstream" / "visa.json"
SOURCES = ROOT / "sources.json"
OUT_JSON = ROOT / "data" / "china-visa-free.json"
OUT_CSV = ROOT / "data" / "china-visa-free.csv"
OUT_PKG = ROOT / "datapackage.json"
OUT_README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"

SITE = "https://chinaeasymode.com"
REPO = "https://github.com/zipengbo/china-visa-free-data"

# ISO 3166-1 alpha-2 by country name; a new country falls back to the Chinese embassy's
# subdomain (gb.china-embassy.gov.cn) and warns so the code can be added here.
ISO2 = json.loads((ROOT / "scripts" / "iso2.json").read_text(encoding="utf-8"))

# (name, type, description) — single source for the CSV header, datapackage and field docs.
FIELDS = [
    ("country", "string", "Country name in English, as used on chinaeasymode.com."),
    ("iso2", "string", "ISO 3166-1 alpha-2 code."),
    ("slug", "string", "URL slug of the country page on chinaeasymode.com."),
    ("entry_policy", "string",
     "Best visa-free entry route for an ordinary visit: `unilateral_visa_free`, `mutual_visa_exemption`, "
     "`transit_240h_only` (no visa-free entry, but 240-hour transit applies) or `visa_required`."),
    ("visa_free_days", "integer", "Maximum stay per entry under the entry policy. Empty when no visa-free entry applies."),
    ("unilateral_days", "integer", "Days allowed under China's unilateral visa-free policy. Empty if the country is not covered."),
    ("unilateral_until", "date",
     "Last day of the unilateral policy (YYYY-MM-DD). Empty when the country is not covered, or when the source data gives no end date."),
    ("mutual_days", "integer", "Days per stay under a mutual visa exemption agreement. Empty if none."),
    ("transit_240h", "boolean", "`true` if nationals qualify for 240-hour (10-day) visa-free transit."),
    ("note_label", "string", "Short heading of a country-specific note, if any."),
    ("note_text", "string", "Country-specific note, if any."),
    ("note_url", "string", "Link backing the note."),
    ("unilateral_source", "string", "Official source for the unilateral policy for this country."),
    ("mutual_source", "string", "Official source for the mutual exemption for this country."),
    ("transit_240h_source", "string", "Official source for 240-hour transit eligibility for this country."),
    ("source_status", "string",
     "`official` (every policy on the row has an official source), `missing_official_source` "
     "(at least one has none yet, see `missing_sources`) or `no_policy_claimed`."),
    ("missing_sources", "string", "Policies on the row that still lack an official source, separated by `;`."),
    ("verified_on", "date", "Date China Easy Mode last verified the upstream data."),
    ("embassy_url", "string", "Chinese embassy in that country."),
    ("guide_url", "string", "China Easy Mode guide for travellers from that country."),
]
FIELD_NAMES = [f[0] for f in FIELDS]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def iso2(country):
    if country["name"] in ISO2:
        return ISO2[country["name"]]
    emb = country.get("embassy") or ""
    if ".china-embassy.gov.cn" in emb:
        return emb.split("//", 1)[-1].split(".", 1)[0].upper()
    return ""


def source_for(policy, country, value, sources):
    """URL of an official source listing this country with matching terms, else ''."""
    for s in sources:
        if not s.get("official") or s["policy"] != policy or country not in s["countries"]:
            continue
        terms = s.get("terms", {})
        if "days" in terms and value.get("days") != terms["days"]:
            continue
        if "until" in terms and value.get("until") != terms["until"]:
            continue
        return s["url"]
    return ""


def build_rows(upstream, srcs):
    rows, warnings = [], []
    official = srcs["sources"]
    for c in upstream["countries"]:
        name = c["name"]
        uni, mut, tr = c.get("unilateral"), c.get("mutual"), bool(c.get("transit240"))
        if uni:
            policy, days = "unilateral_visa_free", uni["days"]
        elif mut:
            policy, days = "mutual_visa_exemption", mut["days"]
        elif tr:
            policy, days = "transit_240h_only", None
        else:
            policy, days = "visa_required", None
        uni_src = source_for("unilateral", name, uni, official) if uni else ""
        mut_src = source_for("mutual", name, mut, official) if mut else ""
        tr_src = source_for("transit_240h", name, {}, official) if tr else ""
        missing = [p for p, claimed, src in (("unilateral", uni, uni_src), ("mutual", mut, mut_src),
                                             ("transit_240h", tr, tr_src)) if claimed and not src]
        claimed = bool(uni or mut or tr)
        note = c.get("note") or {}
        code = iso2(c)
        if name not in ISO2:
            warnings.append(f"{name}: no ISO code (add it to scripts/iso2.json)")
        rows.append({
            "country": name,
            "iso2": code,
            "slug": c["slug"],
            "entry_policy": policy,
            "visa_free_days": days,
            "unilateral_days": uni["days"] if uni else None,
            "unilateral_until": uni.get("until") if uni else None,
            "mutual_days": mut["days"] if mut else None,
            "transit_240h": tr,
            "note_label": note.get("label"),
            "note_text": note.get("text"),
            "note_url": note.get("url"),
            "unilateral_source": uni_src or None,
            "mutual_source": mut_src or None,
            "transit_240h_source": tr_src or None,
            "source_status": ("missing_official_source" if missing else "official") if claimed else "no_policy_claimed",
            "missing_sources": ";".join(missing) or None,
            "verified_on": upstream["lastVerified"],
            "embassy_url": c.get("embassy"),
            "guide_url": f"{SITE}/visa-free/{c['slug']}/",
        })
    # A source listing a country that upstream does not mark for that policy is worth a human look.
    by_name = {c["name"]: c for c in upstream["countries"]}
    for s in official:
        key = {"unilateral": "unilateral", "mutual": "mutual", "transit_240h": "transit240"}[s["policy"]]
        for n in s["countries"]:
            if n not in by_name:
                warnings.append(f"{s['id']}: lists {n}, which is not in upstream")
            elif not by_name[n].get(key):
                warnings.append(f"{s['id']}: lists {n}, but upstream has no {s['policy']} for it")
    return rows, warnings


def dataset(upstream, srcs, rows, version):
    official_urls = {s["url"] for s in srcs["sources"]}
    secondary = list(srcs.get("secondary", []))
    known = official_urls | {s["url"] for s in secondary}
    secondary += [{"url": u, "official": False} for u in upstream.get("sources", []) if u not in known]
    return {
        "name": "China visa-free entry policies by country",
        "description": "Unilateral visa-free entry, mutual visa exemptions and 240-hour visa-free transit "
                       "for travellers to mainland China, one record per country.",
        "publisher": "China Easy Mode",
        "homepage": f"{SITE}/visa/visa-free-entry/",
        "repository": REPO,
        "license": "CC-BY-4.0",
        "attribution": f"China Easy Mode ({SITE})",
        "version": version,
        "verified_on": upstream["lastVerified"],
        "sources": [{k: s[k] for k in ("id", "title", "publisher", "url", "published", "checked_on", "policy", "notes")
                     if k in s} for s in srcs["sources"]],
        "secondary_sources": secondary,
        "countries": rows,
    }


def to_csv(rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELD_NAMES, lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({k: ("true" if v is True else "false" if v is False else "" if v is None else v)
                    for k, v in r.items()})
    return buf.getvalue()


def datapackage(ds):
    return {
        "name": "china-visa-free-data",
        "title": ds["name"],
        "description": ds["description"],
        "homepage": ds["homepage"],
        "version": ds["version"],
        "licenses": [{"name": "CC-BY-4.0", "path": "https://creativecommons.org/licenses/by/4.0/",
                      "title": "Creative Commons Attribution 4.0"}],
        "contributors": [{"title": "China Easy Mode", "path": SITE, "role": "publisher"}],
        "sources": [{"title": s["title"], "path": s["url"]} for s in ds["sources"]],
        "resources": [
            {
                "name": "china-visa-free",
                "path": "data/china-visa-free.csv",
                "format": "csv",
                "mediatype": "text/csv",
                "encoding": "utf-8",
                "schema": {"fields": [{"name": n, "type": t, "description": d} for n, t, d in FIELDS]},
            },
            {"name": "china-visa-free-json", "path": "data/china-visa-free.json", "format": "json",
             "mediatype": "application/json"},
        ],
    }


def fmt_date(iso):
    if not iso:
        return ""
    return dt.date.fromisoformat(iso).strftime("%-d %b %Y")


def readme(ds):
    rows = ds["countries"]
    count = lambda pred: sum(1 for r in rows if pred(r))
    n_uni = count(lambda r: r["unilateral_days"])
    n_mut = count(lambda r: r["mutual_days"])
    n_tr = count(lambda r: r["transit_240h"])
    n_missing = count(lambda r: r["source_status"] == "missing_official_source")
    table = ["| Country | Visa-free entry | Until | 240h transit | Official source | Guide |",
             "|---|---|---|---|---|---|"]
    for r in rows:
        if r["unilateral_days"]:
            entry = f"{r['unilateral_days']} days (unilateral)"
            until = fmt_date(r["unilateral_until"]) or "no end date given"
        elif r["mutual_days"]:
            entry, until = f"{r['mutual_days']} days (mutual)", "no end date"
        else:
            entry, until = "visa required", ""
        src = {"official": "yes", "missing_official_source": "missing: " + (r["missing_sources"] or "").replace(";", ", "),
               "no_policy_claimed": "n/a"}[r["source_status"]]
        table.append(f"| {r['country']} | {entry} | {until} | {'yes' if r['transit_240h'] else 'no'} | {src} "
                     f"| [guide]({r['guide_url']}) |")
    sources = "\n".join(f"- [{s['title']}]({s['url']}) — {s['publisher']}, published {fmt_date(s['published'])}, "
                        f"checked {fmt_date(s['checked_on'])}" + (f". {s['notes']}" if s.get("notes") else "")
                        for s in ds["sources"])
    secondary = "\n".join(f"- {s['url']}" + (f" — {s['publisher']}" if s.get("publisher") else "")
                          for s in ds["secondary_sources"])
    fields = "\n".join(f"| `{n}` | {t} | {d} |" for n, t, d in FIELDS)
    return f"""# China visa-free entry data

Who can enter mainland China without a visa, for how long and until when: unilateral visa-free entry, mutual visa exemptions and 240-hour visa-free transit for {len(rows)} countries, as JSON and CSV. Maintained by [China Easy Mode]({SITE}), a travel guide for foreign visitors to China; the same data powers its [visa-free checker]({SITE}/visa/visa-free-entry/).

**Verified:** {fmt_date(ds['verified_on'])} · **Version:** {ds['version']} · **License:** [CC BY 4.0](LICENSE-DATA) (data), [MIT](LICENSE) (code)

## At a glance

- **{n_uni}** countries: 30-day unilateral visa-free entry
- **{n_mut}** countries: mutual visa exemption
- **{n_tr}** countries: 240-hour (10-day) visa-free transit
- **{n_missing}** rows still need an official source for at least one policy (see `source_status`)

## Download

| File | Use |
|---|---|
| [`data/china-visa-free.csv`](data/china-visa-free.csv) | Spreadsheets, pandas, R |
| [`data/china-visa-free.json`](data/china-visa-free.json) | Apps and scripts; includes dataset metadata and sources |
| [`datapackage.json`](datapackage.json) | [Frictionless Data](https://frictionlessdata.io/) descriptor |

Stable raw URLs:

```
https://raw.githubusercontent.com/zipengbo/china-visa-free-data/main/data/china-visa-free.csv
https://raw.githubusercontent.com/zipengbo/china-visa-free-data/main/data/china-visa-free.json
```

## How to use

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/zipengbo/china-visa-free-data/main/data/china-visa-free.csv")
df[df.entry_policy == "unilateral_visa_free"][["country", "unilateral_until"]]
```

```js
const res = await fetch("https://raw.githubusercontent.com/zipengbo/china-visa-free-data/main/data/china-visa-free.json");
const {{ countries }} = await res.json();
const jp = countries.find((c) => c.iso2 === "JP");
```

## Countries

{chr(10).join(table)}

"Visa required" means no national visa-free entry at the time of verification; countries not in the table are not covered by any of these policies. Regional schemes (Hainan, Guangxi ASEAN tour groups, cruise and Hong Kong/Macau tour arrangements) are out of scope. Every traveller also needs a valid passport and, for transit, a confirmed onward ticket to a third country or region; always check the official notice before you fly.

## Fields

| Field | Type | Description |
|---|---|---|
{fields}

Empty means "not applicable" or "not known"; nothing is filled in by guesswork.

## Sources

Official sources (each country is linked to a source only after the document itself was read and lists that country with the same terms):

{sources}

Other references used by China Easy Mode (not counted as official):

{secondary}

Missing a source for your country? Open an issue with a link to an official notice (NIA, Ministry of Foreign Affairs or a Chinese embassy/consulate).

## Updates

The data is generated from China Easy Mode's own visa data. When the site's data changes, a new version is built and committed here automatically, and [CHANGELOG.md](CHANGELOG.md) records what changed.

## License and attribution

Data: [Creative Commons Attribution 4.0](LICENSE-DATA). You may share and adapt it, including commercially, as long as you credit China Easy Mode with a link:

> Data: [China Easy Mode]({SITE}) — China visa-free entry data, CC BY 4.0

Code (`scripts/`): [MIT](LICENSE).

This dataset is travel information, not legal advice. Border officers make the final decision at entry.
"""


def changelog_entry(old, new, today, commit):
    lines = []
    old_rows = {r["country"]: r for r in (old or {}).get("countries", [])}
    new_rows = {r["country"]: r for r in new["countries"]}
    if not old_rows:
        lines.append(f"- Initial release: {len(new_rows)} countries, verified {new['verified_on']}.")
    else:
        for n in sorted(new_rows.keys() - old_rows.keys()):
            lines.append(f"- Added {n} ({new_rows[n]['entry_policy']}).")
        for n in sorted(old_rows.keys() - new_rows.keys()):
            lines.append(f"- Removed {n}.")
        for n in sorted(new_rows.keys() & old_rows.keys()):
            a, b = old_rows[n], new_rows[n]
            diffs = [f"`{k}` {a.get(k)!r} → {b.get(k)!r}" for k in FIELD_NAMES
                     if k != "verified_on" and a.get(k) != b.get(k)]
            if diffs:
                lines.append(f"- {n}: " + "; ".join(diffs))
        if old.get("verified_on") != new["verified_on"]:
            lines.append(f"- Re-verified on {new['verified_on']}.")
        if [s["url"] for s in old.get("sources", [])] != [s["url"] for s in new["sources"]]:
            lines.append("- Official source list updated.")
    if not lines:
        return ""
    head = f"## {today}" + (f" — synced from chinaeasymode@{commit[:7]}" if commit else "")
    return head + "\n\n" + "\n".join(lines) + "\n"


def comparable(ds):
    return {k: v for k, v in ds.items() if k != "version"} if ds else None


def main():
    check = "--check" in sys.argv
    upstream, srcs = load(UPSTREAM), load(SOURCES)
    rows, warnings = build_rows(upstream, srcs)
    for w in warnings:
        print("warning:", w, file=sys.stderr)
    old = load(OUT_JSON) if OUT_JSON.exists() else None
    today = os.environ.get("BUILD_DATE") or dt.date.today().isoformat()
    ds = dataset(upstream, srcs, rows, old["version"] if old else today)
    changed = comparable(ds) != comparable(old)
    if changed:
        ds["version"] = today
    outputs = {
        OUT_JSON: json.dumps(ds, indent=2, ensure_ascii=False) + "\n",
        OUT_CSV: to_csv(rows),
        OUT_PKG: json.dumps(datapackage(ds), indent=2, ensure_ascii=False) + "\n",
        OUT_README: readme(ds),
    }
    if check:
        stale = [p.name for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        if stale or changed:
            print("stale:", ", ".join(stale) or "data", "- run python3 scripts/build.py", file=sys.stderr)
            sys.exit(1)
        print("up to date")
        return
    for p, text in outputs.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    if changed:
        entry = changelog_entry(old, ds, today, os.environ.get("SOURCE_COMMIT", ""))
        if entry:
            prev = CHANGELOG.read_text(encoding="utf-8") if CHANGELOG.exists() else ""
            body = prev.split("\n", 2)[2] if prev.startswith("# Changelog") else prev
            CHANGELOG.write_text("# Changelog\n\n" + entry + ("\n" + body.lstrip("\n") if body.strip() else ""),
                                 encoding="utf-8")
    print(("updated" if changed else "no data change") + f", version {ds['version']}")


if __name__ == "__main__":
    main()
