# China visa-free entry data

Who can enter mainland China without a visa, for how long and until when: unilateral visa-free entry, mutual visa exemptions and 240-hour visa-free transit for 102 countries, as JSON and CSV. Maintained by [China Easy Mode](https://chinaeasymode.com), a travel guide for foreign visitors to China; the same data powers its [visa-free checker](https://chinaeasymode.com/visa/visa-free-entry/).

**Verified:** 18 Oct 2026 · **Version:** 2026-10-26 · **License:** [CC BY 4.0](LICENSE-DATA) (data), [MIT](LICENSE) (code)

## At a glance

- **50** countries: 30-day unilateral visa-free entry
- **29** countries: mutual visa exemption
- **57** countries: 240-hour (10-day) visa-free transit
- **7** rows still need an official source for at least one policy (see `source_status`)

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
const { countries } = await res.json();
const jp = countries.find((c) => c.iso2 === "JP");
```

## Countries

| Country | Visa-free entry | Until | 240h transit | Official source | Guide |
|---|---|---|---|---|---|
| Albania | 90 days (mutual) | no end date | yes | missing: mutual | [guide](https://chinaeasymode.com/visa-free/albania/) |
| Andorra | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/andorra/) |
| Antigua and Barbuda | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/antigua-and-barbuda/) |
| Argentina | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/argentina/) |
| Armenia | 90 days (mutual) | no end date | no | missing: mutual | [guide](https://chinaeasymode.com/visa-free/armenia/) |
| Australia | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/australia/) |
| Austria | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/austria/) |
| Azerbaijan | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/azerbaijan/) |
| Bahamas | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/bahamas/) |
| Bahrain | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/bahrain/) |
| Bangladesh | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/bangladesh/) |
| Barbados | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/barbados/) |
| Belarus | 30 days (mutual) | no end date | yes | yes | [guide](https://chinaeasymode.com/visa-free/belarus/) |
| Belgium | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/belgium/) |
| Bosnia and Herzegovina | 90 days (mutual) | no end date | yes | missing: mutual | [guide](https://chinaeasymode.com/visa-free/bosnia-and-herzegovina/) |
| Brazil | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/brazil/) |
| Brunei | 30 days (unilateral) | no end date given | yes | missing: unilateral | [guide](https://chinaeasymode.com/visa-free/brunei/) |
| Bulgaria | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/bulgaria/) |
| Canada | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/canada/) |
| Chile | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/chile/) |
| Colombia | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/colombia/) |
| Croatia | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/croatia/) |
| Cyprus | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/cyprus/) |
| Czech Republic | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/czech-republic/) |
| Denmark | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/denmark/) |
| Dominica | 30 days (mutual) | no end date | no | missing: mutual | [guide](https://chinaeasymode.com/visa-free/dominica/) |
| Ecuador | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/ecuador/) |
| Egypt | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/egypt/) |
| Estonia | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/estonia/) |
| Fiji | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/fiji/) |
| Finland | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/finland/) |
| France | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/france/) |
| Georgia | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/georgia/) |
| Germany | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/germany/) |
| Ghana | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/ghana/) |
| Greece | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/greece/) |
| Grenada | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/grenada/) |
| Hungary | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/hungary/) |
| Iceland | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/iceland/) |
| India | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/india/) |
| Indonesia | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/indonesia/) |
| Ireland | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/ireland/) |
| Israel | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/israel/) |
| Italy | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/italy/) |
| Japan | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/japan/) |
| Kazakhstan | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/kazakhstan/) |
| Kenya | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/kenya/) |
| Kuwait | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/kuwait/) |
| Kyrgyzstan | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/kyrgyzstan/) |
| Latvia | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/latvia/) |
| Liechtenstein | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/liechtenstein/) |
| Lithuania | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/lithuania/) |
| Luxembourg | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/luxembourg/) |
| Malaysia | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/malaysia/) |
| Maldives | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/maldives/) |
| Malta | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/malta/) |
| Mauritius | 60 days (mutual) | no end date | no | missing: mutual | [guide](https://chinaeasymode.com/visa-free/mauritius/) |
| Mexico | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/mexico/) |
| Monaco | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/monaco/) |
| Montenegro | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/montenegro/) |
| Morocco | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/morocco/) |
| Nepal | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/nepal/) |
| Netherlands | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/netherlands/) |
| New Zealand | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/new-zealand/) |
| Nigeria | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/nigeria/) |
| North Macedonia | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/north-macedonia/) |
| Norway | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/norway/) |
| Oman | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/oman/) |
| Pakistan | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/pakistan/) |
| Peru | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/peru/) |
| Philippines | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/philippines/) |
| Poland | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/poland/) |
| Portugal | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/portugal/) |
| Qatar | 30 days (mutual) | no end date | yes | yes | [guide](https://chinaeasymode.com/visa-free/qatar/) |
| Romania | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/romania/) |
| Russia | 30 days (unilateral) | 31 Dec 2027 | yes | yes | [guide](https://chinaeasymode.com/visa-free/russia/) |
| Samoa | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/samoa/) |
| San Marino | 90 days (mutual) | no end date | no | missing: mutual | [guide](https://chinaeasymode.com/visa-free/san-marino/) |
| Saudi Arabia | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/saudi-arabia/) |
| Serbia | 30 days (mutual) | no end date | yes | yes | [guide](https://chinaeasymode.com/visa-free/serbia/) |
| Seychelles | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/seychelles/) |
| Singapore | 30 days (mutual) | no end date | yes | yes | [guide](https://chinaeasymode.com/visa-free/singapore/) |
| Slovakia | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/slovakia/) |
| Slovenia | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/slovenia/) |
| Solomon Islands | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/solomon-islands/) |
| South Africa | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/south-africa/) |
| South Korea | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/south-korea/) |
| Spain | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/spain/) |
| Sri Lanka | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/sri-lanka/) |
| Suriname | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/suriname/) |
| Sweden | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/sweden/) |
| Switzerland | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/switzerland/) |
| Thailand | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/thailand/) |
| Tonga | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/tonga/) |
| Turkey | visa required |  | no | n/a | [guide](https://chinaeasymode.com/visa-free/turkey/) |
| Ukraine | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/ukraine/) |
| United Arab Emirates | 30 days (mutual) | no end date | yes | yes | [guide](https://chinaeasymode.com/visa-free/united-arab-emirates/) |
| United Kingdom | 30 days (unilateral) | 31 Dec 2026 | yes | yes | [guide](https://chinaeasymode.com/visa-free/united-kingdom/) |
| United States | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/united-states/) |
| Uruguay | 30 days (unilateral) | 31 Dec 2026 | no | yes | [guide](https://chinaeasymode.com/visa-free/uruguay/) |
| Uzbekistan | 30 days (mutual) | no end date | no | yes | [guide](https://chinaeasymode.com/visa-free/uzbekistan/) |
| Vietnam | visa required |  | yes | yes | [guide](https://chinaeasymode.com/visa-free/vietnam/) |

"Visa required" means no national visa-free entry at the time of verification; countries not in the table are not covered by any of these policies. Regional schemes (Hainan, Guangxi ASEAN tour groups, cruise and Hong Kong/Macau tour arrangements) are out of scope. Every traveller also needs a valid passport and, for transit, a confirmed onward ticket to a third country or region; always check the official notice before you fly.

## Fields

| Field | Type | Description |
|---|---|---|
| `country` | string | Country name in English, as used on chinaeasymode.com. |
| `iso2` | string | ISO 3166-1 alpha-2 code. |
| `slug` | string | URL slug of the country page on chinaeasymode.com. |
| `entry_policy` | string | Best visa-free entry route for an ordinary visit: `unilateral_visa_free`, `mutual_visa_exemption`, `transit_240h_only` (no visa-free entry, but 240-hour transit applies) or `visa_required`. |
| `visa_free_days` | integer | Maximum stay per entry under the entry policy. Empty when no visa-free entry applies. |
| `unilateral_days` | integer | Days allowed under China's unilateral visa-free policy. Empty if the country is not covered. |
| `unilateral_until` | date | Last day of the unilateral policy (YYYY-MM-DD). Empty when the country is not covered, or when the source data gives no end date. |
| `mutual_days` | integer | Days per stay under a mutual visa exemption agreement. Empty if none. |
| `transit_240h` | boolean | `true` if nationals qualify for 240-hour (10-day) visa-free transit. |
| `note_label` | string | Short heading of a country-specific note, if any. |
| `note_text` | string | Country-specific note, if any. |
| `note_url` | string | Link backing the note. |
| `unilateral_source` | string | Official source for the unilateral policy for this country. |
| `mutual_source` | string | Official source for the mutual exemption for this country. |
| `transit_240h_source` | string | Official source for 240-hour transit eligibility for this country. |
| `source_status` | string | `official` (every policy on the row has an official source), `missing_official_source` (at least one has none yet, see `missing_sources`) or `no_policy_claimed`. |
| `missing_sources` | string | Policies on the row that still lack an official source, separated by `;`. |
| `verified_on` | date | Date China Easy Mode last verified the upstream data. |
| `embassy_url` | string | Chinese embassy in that country. |
| `guide_url` | string | China Easy Mode guide for travellers from that country. |

Empty means "not applicable" or "not known"; nothing is filled in by guesswork.

## Sources

Official sources (each country is linked to a source only after the document itself was read and lists that country with the same terms):

- [Visa-Free Transit Policies](https://en.nia.gov.cn/n147418/n147463/c183412/content.html) — National Immigration Administration of China, published 20 Aug 2026, checked 26 Oct 2026
- [Notice on the Extension of the Unilateral Visa-Free Policy](https://losangeles.china-consulate.gov.cn/eng/visa/Notice/202511/t20251104_11746357.htm) — Consulate General of the People's Republic of China in Los Angeles, published 4 Nov 2025, checked 26 Oct 2026
- [Notice Regarding the Implementation of Visa-Free Policies for Canada and the United Kingdom](https://english.shanghai.gov.cn/en-PolicyLibrary-EntryExit/20260818/8aa6aa1bc34b4228be0c87a14c75875f.html) — Ministry of Foreign Affairs of China (published by Shanghai Municipal People's Government), published 15 Feb 2026, checked 26 Oct 2026
- [China extends visa-free policy for Russia to Dec 31, 2027](https://english.shanghai.gov.cn/en-VisaLatest/20260520/0b86f04686c84c4a8bdca4f77dbee1eb.html) — Ministry of Foreign Affairs spokesperson, as published by Shanghai Municipal People's Government, published 20 May 2026, checked 26 Oct 2026
- [Mutual Visa Exemption List](https://cs.mfa.gov.cn/lh/lhqz_149493/list/202607/t20260713_11981384.html) — China Consular Service, Ministry of Foreign Affairs of China, published 13 Jul 2026, checked 26 Oct 2026. The list states a general stay of under 30 days and lists agreements covering ordinary passports for the countries above. It also lists ordinary-passport agreements for Albania, Armenia, Bosnia and Herzegovina, Mauritius and San Marino but does not state their 60/90-day stays, so those are not linked. For Dominica it lists only Dominican ordinary passports for public affairs.

Other references used by China Easy Mode (not counted as official):

- https://www.china-briefing.com/news/china-visa-free-travel-policies-complete-guide/ — China Briefing (Dezan Shira & Associates)

Missing a source for your country? Open an issue with a link to an official notice (NIA, Ministry of Foreign Affairs or a Chinese embassy/consulate).

## Updates

The data is generated from China Easy Mode's own visa data. When the site's data changes, a new version is built and committed here automatically, and [CHANGELOG.md](CHANGELOG.md) records what changed.

## License and attribution

Data: [Creative Commons Attribution 4.0](LICENSE-DATA). You may share and adapt it, including commercially, as long as you credit China Easy Mode with a link:

> Data: [China Easy Mode](https://chinaeasymode.com) — China visa-free entry data, CC BY 4.0

Code (`scripts/`): [MIT](LICENSE).

This dataset is travel information, not legal advice. Border officers make the final decision at entry.
