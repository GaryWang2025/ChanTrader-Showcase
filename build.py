#!/usr/bin/env python3
"""Reproducible, dependency-free static-site build."""
from pathlib import Path
from shutil import copytree, rmtree

root = Path(__file__).resolve().parent
source, output = root / "src", root / "dist"
if output.exists(): rmtree(output)
copytree(source, output)
print(f"Static build written to {output}")
