import sys
import re
from pathlib import Path

def extract_version_notes(changelog_path: str, version_tag: str, output_path: str):
    content = Path(changelog_path).read_text()
    pattern = rf"(##\s+{re.escape(version_tag)}\b.*?)(?=\n##\s+|\Z)"  # non-greedy match until next ##

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"❌ Version section '{version_tag}' not found in CHANGELOG.md")
        sys.exit(1)

    Path(output_path).write_text(match.group(1).strip())
    print(f"✅ Extracted changelog for {version_tag} → {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: extract_changelog.py <CHANGELOG.md> <version> <output.md>")
        sys.exit(1)

    extract_version_notes(*sys.argv[1:])
