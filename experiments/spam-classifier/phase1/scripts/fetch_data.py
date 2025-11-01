"""Download the SMS spam dataset and save to the local data directory.

Usage:
    python fetch_data.py
"""
from __future__ import annotations
import os
import sys
from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv"


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def download(url: str, out_path: str) -> None:
    print(f"Downloading {url} -> {out_path}")
    with urlopen(url) as response, open(out_path, "wb") as out_file:
        out_file.write(response.read())


def main() -> int:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    data_dir = os.path.join(root, "data")
    ensure_dir(data_dir)
    out_file = os.path.join(data_dir, "sms_spam_no_header.csv")

    try:
        download(URL, out_file)
    except Exception as e:
        print("Failed to download dataset:", e, file=sys.stderr)
        return 2

    # Quick sanity check: print number of lines and class distribution
    try:
        with open(out_file, "r", encoding="utf-8", errors="replace") as f:
            lines = [l.rstrip("\n") for l in f if l.strip()]
        print(f"Downloaded {len(lines)} non-empty lines to {out_file}")
        # count labels (first token until comma)
        labels = [l.split(",", 1)[0].strip() for l in lines]
        from collections import Counter

        c = Counter(labels)
        print("Label distribution:")
        for k, v in c.items():
            print(f"  {k}: {v}")
    except Exception as e:
        print("Downloaded file present but failed to read/inspect:", e, file=sys.stderr)
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
