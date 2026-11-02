#!/usr/bin/env python3
"""Convert approved Kora PDFs into GitHub-editable Markdown.
Keeps PDF content and extracts the non-text schema diagram as an image.
"""
from pathlib import Path
import fitz
import re

BASE=Path("project packs/Kora/Kora - 2025 only")
GUIDES=[
 ("Kora 2025 Project Guide.pdf","Kora 2025 Project Guide.md"),
 ("Kora 2025 Database Setup Guide.pdf","Kora 2025 Database Setup Guide.md"),
]
FOOTER="CadencePlus Solutions™ · Synthetic training data · Currency NGN · Orders placed in 2025 · Snapshot 31 December 2025"
def extract(pdf,name):
    doc=fitz.open(pdf)
    blocks=[]
    for page_number,page in enumerate(doc):
        # Database schema is a vector diagram embedded in the approved PDF.
        if name.startswith("Kora 2025 Project") and page_number==1:
            clip=fitz.Rect(35,392,575,697)
            pix=page.get_pixmap(matrix=fitz.Matrix(2,2),clip=clip,alpha=False)
            pix.save(BASE/"Kora 2025 Database Schema.png")
        entries=[]
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block: continue
            lines=block["lines"]
            spans=[s for ln in lines for s in ln["spans"]]
            if not spans: continue
            y=block["bbox"][1]
            if y>705: continue
            text=" ".join("".join(s["text"] for s in line["spans"]).strip() for line in lines).strip()
            if not text or text==FOOTER or re.fullmatch(r"[0-9]+",text): continue
            if text.startswith("CadencePlus Solutions™ · Synthetic training data"):continue
            text=text.replace("\x00","").strip()
            if not text:continue
            fontsize=max(s["size"] for s in spans)
            entries.append((y,text,fontsize))
        entries.sort(key=lambda e:e[0])
        blocks.extend(entries)
    out=[f"<!-- Editable GitHub source for {name}. Edit using GitHub's pencil icon. -->",""]
    current=[]
    def flush():
        if current:
            out.append(" ".join(current).strip())
            out.append("")
            current.clear()
    for i,(y,t,size) in enumerate(blocks):
        if size>=20:
            flush();out.append(("# " if not any(line.startswith("# ") for line in out) else "## ")+t+"\n")
        elif size>=13.5 and (len(t)<85):
            flush();out.append("### "+t+"\n")
            if t=="Database Schema" and name.startswith("Kora 2025 Project"):
                out.append("![Kora database schema diagram](Kora%202025%20Database%20Schema.png)\n")
        elif t.startswith("•"):
            flush();out.append("- "+t[1:].strip())
        elif re.match(r"^\d+\.\s",t):
            flush();out.append(t)
        elif t.startswith("**") and not t.endswith("**"):
            flush();out.append("*"+t.lstrip("*").strip()+"*")
        else:
            if out and (out[-1].startswith("- ") or re.match(r"^\d+\.\s",out[-1])):
                out[-1]+=" "+t
            else:
                current.append(t)
    flush()
    text="\n".join(out).replace("Kora-2025-only.pdf","Kora 2025 Project Guide.md")
    # Preserve intended bullet lost in the source PDF's text flow.
    if name.startswith("Kora 2025 Project"):
        text=text.replace("- Investigate two business questions.","- Load a local database (see Database Setup Guide for details).\n- Investigate two business questions.",1)
        text=text.replace("Load a local database (see Database Setup Guide for details).\n\n","")
    else:
        text=text.replace("Choose one database engine. The same seven tables are provided in both routes. The CSVs are optional for Excel or Power BI; the SQL loaders already contain all data, so you do not need to import seven CSVs manually.","Choose a database engine and follow the applicable instructions.")
    target=BASE/name.replace(".pdf",".md")
    target.write_text(text,encoding="utf-8")
    print(target,len(text),"characters")
for source,target in GUIDES:
    if not (BASE/source).is_file(): raise SystemExit(f"Missing PDF: {BASE/source}")
    extract(BASE/source,target)
