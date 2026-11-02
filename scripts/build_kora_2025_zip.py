#!/usr/bin/env python3
"""Rebuild Kora 2025 ZIP from the exact project directory checked out from GitHub."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import sys

root = Path(__file__).resolve().parents[1]
pack = root / "project packs" / "Kora" / "Kora - 2025 only"
zip_path = pack / "Kora-2025-only.zip"
required = [
    pack / "Kora 2025 Project Guide.pdf",
    pack / "Kora 2025 Database Setup Guide.pdf",
]
missing = [str(p.relative_to(root)) for p in required if not p.is_file()]
if missing:
    sys.exit("Cannot publish Kora ZIP. First upload the approved PDFs:\n" + "\n".join(missing))
excluded = {
    "Kora-2025-only.zip",
    "Kora-2025-only.pdf",
    "Kora-2025-only-REVIEW.pdf",
}
obsolete = pack / "Database" / "README_PostgreSQL_MySQL.md"
paths = [
    p for p in pack.rglob("*")
    if p.is_file() and p != zip_path and p.name not in excluded and p != obsolete
    and not any(part.startswith(".") for part in p.relative_to(pack).parts)
]
with ZipFile(zip_path, "w", compression=ZIP_DEFLATED, compresslevel=8) as z:
    for file in sorted(paths):
        z.write(file, arcname=str(Path(pack.name) / file.relative_to(pack)))
with ZipFile(zip_path) as z:
    assert z.testzip() is None, "Archive CRC check failed"
    actual = set(z.namelist())
    expected = {str(Path(pack.name) / p.relative_to(pack)) for p in paths}
    assert actual == expected, "ZIP files do not match repository contents"
    assert not any(name.endswith("Kora-2025-only.zip") for name in actual)
    print(f"Validated {zip_path}: {len(actual)} files, {zip_path.stat().st_size:,} bytes")
