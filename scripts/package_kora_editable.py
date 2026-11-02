#!/usr/bin/env python3
"""Package exactly the GitHub-editable Kora 2025 tree (except the ZIP itself)."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
pack=Path("project packs/Kora/Kora - 2025 only")
required=[pack/"Kora 2025 Project Guide.md",pack/"Kora 2025 Database Setup Guide.md",pack/"Kora 2025 Database Schema.png"]
for p in required:
    assert p.is_file(), f"Missing: {p}"
old=[pack/"Kora 2025 Project Guide.pdf",pack/"Kora 2025 Database Setup Guide.pdf",pack/"Kora-2025-only.pdf",pack/"Database/README_PostgreSQL_MySQL.md"]
for p in old:
    if p.exists(): p.unlink()
archive=pack/"Kora-2025-only.zip"
files=sorted(p for p in pack.rglob("*") if p.is_file() and p!=archive and ".git" not in p.parts)
with ZipFile(archive,"w",ZIP_DEFLATED,compresslevel=8) as out:
    for p in files:
        out.write(p,arcname=str(Path(pack.name)/p.relative_to(pack)))
with ZipFile(archive) as z:
    assert z.testzip() is None
    actual=set(z.namelist())
    expected={str(Path(pack.name)/p.relative_to(pack)) for p in files}
    assert actual==expected
    assert not any(name.lower().endswith(".zip") for name in actual)
    for f in ["Kora 2025 Project Guide.md","Kora 2025 Database Setup Guide.md","Database/PostgreSQL/01_Load_Kora_Starter.sql","Database/MySQL/01_Load_Kora_Starter.sql","Database/SQLite/01_Load_Kora_Starter.sql","Database/SQL_Server/01_Load_Kora_Starter.sql"]:
        assert str(Path(pack.name)/f) in actual, f
print(f"ZIP validated: {len(files)} files; {archive.stat().st_size} bytes")
