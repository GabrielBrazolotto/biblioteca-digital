# src/biblioteca/core.py
from pathlib import Path
import re
from typing import Optional

SUPPORTED_EXTS = {".pdf", ".epub", ".mobi", ".txt"}

def is_supported(file: Path) -> bool:
    return file.is_file() and file.suffix.lower() in SUPPORTED_EXTS

YEAR_RE = re.compile(r"(?:(?:19|20)\d{2})")

def guess_year_from_name(name: str) -> Optional[int]:
    m = YEAR_RE.search(name)
    return int(m.group()) if m else None

def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def normalize_name(name: str) -> str:
    return re.sub(r"\s+", "_", name.strip())
