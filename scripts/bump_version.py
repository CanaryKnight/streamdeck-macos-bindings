# scripts/bump_version.py

import json
from pathlib import Path
import sys

def bump_version(manifest_path: str):
    p = Path(manifest_path)
    if not p.exists():
        print(f"❌ Manifest not found: {manifest_path}")
        sys.exit(1)

    data = json.load(p.open())
    version_str = data.get("Version", "0.1.0.0")
    segments = list(map(int, version_str.split(".")))
    segments[-1] += 1
    new_version = ".".join(map(str, segments))
    data["Version"] = new_version
    json.dump(data, p.open("w"), indent=2)
    print(f"✅ New version: {new_version}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py <path-to-manifest.json>")
        sys.exit(1)

    bump_version(sys.argv[1])
