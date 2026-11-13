# Portfolio site

Static site for Shirley Gray's group at Northbridge University. Every page is
generated from Markdown, and shared tables live in `_data/`.

## Layout

- `content/projects/*.md` — one file per project: YAML front matter plus abstract
- `_data/repro_index.json` — reproducibility index backing the "Reproduce" page
- `_layouts/` — page templates
- `scripts/validate_site.py` — sanity checks executed by the build
