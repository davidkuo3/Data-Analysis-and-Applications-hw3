"""Train a baseline SVM classifier for the SMS spam dataset.

Saves model+vectorizer using joblib and writes a JSON metrics report.

Usage:
    python train_baseline.py --data data/sms_spam_no_header.csv
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
import joblib


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=str, default="data/sms_spam_no_header.csv")
    p.add_argument("--output-model", type=str, default="models/baseline_svm.joblib")
    p.add_argument("--metrics", type=str, default="reports/phase1_metrics.json")
    p.add_argument("--test-size", type=float, default=0.2)
    return p.parse_args()


def prepare_dirs(path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def load_data(csv_path: str) -> pd.DataFrame:
    # The CSV has no header: first column label, second column text
    df = pd.read_csv(csv_path, header=None, names=["label", "text"], encoding="latin-1")
    return df


def main() -> int:
    args = parse_args()
    data_path = os.path.abspath(args.data)

    if not os.path.exists(data_path):
        print(f"Data file not found: {data_path}")
        return 2

    df = load_data(data_path)
    # normalize labels: ham -> 0, spam -> 1
    df = df.dropna(subset=["text", "label"]).reset_index(drop=True)
    df["label_num"] = df["label"].map({"ham": 0, "spam": 1})

    X = df["text"].astype(str).values
    y = df["label_num"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)
    X_train_t = vectorizer.fit_transform(X_train)
    X_test_t = vectorizer.transform(X_test)

    clf = LinearSVC(random_state=42)
    clf.fit(X_train_t, y_train)

    preds = clf.predict(X_test_t)

    acc = accuracy_score(y_test, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, preds, average="binary")
    cm = confusion_matrix(y_test, preds).tolist()

    metrics = {
        "accuracy": float(acc),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "confusion_matrix": cm,
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
    }

    prepare_dirs(args.output_model)
    joblib.dump({"model": clf, "vectorizer": vectorizer}, args.output_model)
    print(f"Saved model+vectorizer to {args.output_model}")

    prepare_dirs(args.metrics)
    with open(args.metrics, "w", encoding="utf-8") as fh:
        json.dump(metrics, fh, indent=2)
    print(f"Saved metrics to {args.metrics}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
