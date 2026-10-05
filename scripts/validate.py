#!/usr/bin/env python3
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "engines.json"
VALID_CATEGORIES = {"general-2d-3d", "2d-focused", "3d-focused", "frameworks", "specialized", "legacy"}
REQUIRED = {"name", "category", "type", "dimensions", "languages", "license", "workflow", "website", "source", "notes"}

def valid_url(value: str) -> bool:
    try:
        u = urlparse(value)
        return u.scheme in {"http", "https"} and bool(u.netloc)
    except Exception:
        return False

def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    engines = data.get("engines", [])
    errors = []
    seen = set()
    for i, e in enumerate(engines, 1):
        missing = REQUIRED - set(e)
        if missing:
            errors.append(f"#{i} missing fields: {sorted(missing)}")
        name = e.get("name", "")
        key = name.casefold()
        if key in seen:
            errors.append(f"duplicate name: {name}")
        seen.add(key)
        if e.get("category") not in VALID_CATEGORIES:
            errors.append(f"{name}: invalid category {e.get('category')!r}")
        for field in ("website", "source"):
            if not valid_url(e.get(field, "")):
                errors.append(f"{name}: invalid {field} URL")
        for field in REQUIRED - {"website", "source"}:
            if not isinstance(e.get(field), str) or not e.get(field, "").strip():
                errors.append(f"{name or '#'+str(i)}: blank/non-string field {field}")
    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1
    print(f"OK: {len(engines)} entries validated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
