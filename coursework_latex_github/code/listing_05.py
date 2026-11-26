import json
from pathlib import Path
MAX_PARTS = 3
        style = entry.get("style", "")
        source = entry.get("source", "unknown")
        if not style:
            continue
        try:
            clean = normalize(name)
        except ValueError:
            continue
        parts = count_parts(clean)
        if not (1 <= parts <= MAX_PARTS):
            continue
        key = (clean.lower(), style)
        if key in result:
            continue
        result[key] = {
            "name": clean,
            "style": style,
            "source": source,
            "parts": parts,
        }
    return list(result.values())
if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    for src, out in [
        ("seed_plants.json", "plants_clean.json"),
        ("products.json", "products_clean.json"),
    ]:
        with (root / "data" / src).open("r", encoding="utf-8") as f:
            raw = json.load(f)
        cleaned = preprocess(raw)
        with (root / "data" / out).open("w", encoding="utf-8") as f:
            json.dump(cleaned, f, ensure_ascii=False, indent=2)
        print(f"{src}: {len(raw)} → {len(cleaned)} → {out}")
