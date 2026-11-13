#!/usr/bin/env python3
"""Sanity checks for the site data files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "repro_index.json"


def main():
    index = json.loads(DATA.read_text())
    for slug, entry in index.items():
        assert isinstance(entry.get("repo"), str), slug
        params = entry.get("parameters")
        assert isinstance(params, list) and params, slug
        for p in params:
            assert set(p) == {"name", "type", "default", "description"}, (slug, p)
            assert isinstance(p["name"], str), (slug, p["name"])
            # The template prints the stored value directly.
            assert isinstance(p["type"], str), f"{slug}:{p['name']} type must be a string"
    print(f"OK: {len(index)} projects")


if __name__ == "__main__":
    main()
