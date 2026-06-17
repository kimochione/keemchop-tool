#!/usr/bin/env python3
"""
llama.cpp Tools Restore Script
Generated: 2026-06-17 05:59:55

Downloads all llama.cpp tools from GitHub to a fresh VM.
"""

import os
import sys
import requests
from pathlib import Path

RAW_BASE = "https://raw.githubusercontent.com/kimochione/keemchop-tool/main/llama-cpp-tools"

BINARY_FILES = ['llama-quantize']
SCRIPT_FILES = ['convert_hf_to_gguf.py', 'convert_llama_ggml_to_gguf.py']

OUTPUT_DIR = Path("/content/llama.cpp")
BIN_DIR = OUTPUT_DIR / "build" / "bin"

def download(url, dest, executable=False):
    print(f"   Downloading {dest.name}...", end=" ")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(dest, 'wb') as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    if executable:
        dest.chmod(0o755)
    print(f"OK ({dest.stat().st_size:,} bytes)")

print("=" * 60)
print("llama.cpp Tools Restore")
print("=" * 60)

BIN_DIR.mkdir(parents=True, exist_ok=True)

for f in BINARY_FILES:
    url = f"{RAW_BASE}/bin/{f}"
    download(url, BIN_DIR / f, executable=True)

for f in SCRIPT_FILES:
    url = f"{RAW_BASE}/scripts/{f}"
    download(url, OUTPUT_DIR / f, executable=True)

print("\nDone! Tools restored to", OUTPUT_DIR)
