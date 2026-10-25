# Contributing

Corrections are welcome, especially official sources for rows marked `missing_official_source`.

- Open an issue with a link to an official notice (National Immigration Administration, Ministry of Foreign Affairs, or a Chinese embassy or consulate) and what it changes.
- Files in `data/`, `datapackage.json` and `README.md` are generated: do not edit them by hand. Country facts come from `upstream/visa.json`, which is synced from China Easy Mode; source links live in `sources.json`.
- After changing `sources.json`, run `python3 scripts/build.py` and commit the result.
