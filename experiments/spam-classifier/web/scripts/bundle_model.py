"""Copy the Phase 2 model into the web/models directory for easy deployment.

Usage:
    python bundle_model.py
"""
from __future__ import annotations
import shutil
import os
from pathlib import Path


def main() -> int:
    # file path: .../experiments/spam-classifier/web/scripts/bundle_model.py
    # parents[0]=scripts, [1]=web, [2]=spam-classifier, [3]=experiments, [4]=hw3 (repo root)
    repo_root = Path(__file__).parents[4]
    src = repo_root / "experiments" / "spam-classifier" / "phase1" / "models" / "phase2_logreg.joblib"
    dst_dir = repo_root / "experiments" / "spam-classifier" / "web" / "models"
    dst = dst_dir / "phase2_logreg.joblib"

    if not src.exists():
        print(f"Source model not found: {src}")
        return 2

    dst_dir.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(src, dst)
        print(f"Copied {src} -> {dst}")
    except Exception as e:
        print("Failed to copy model:", e)
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
