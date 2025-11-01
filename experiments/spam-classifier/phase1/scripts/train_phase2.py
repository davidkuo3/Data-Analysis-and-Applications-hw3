"""Phase 2 training: Logistic Regression + AUC/PR-AUC metrics and comparison to Phase 1 baseline.

Usage:
    python train_phase2.py --data <path-to-csv>
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    roc_auc_score,
    average_precision_score,
)
import joblib


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--data", type=str, default="data/sms_spam_no_header.csv")
    p.add_argument("--output-model", type=str, default="models/phase2_logreg.joblib")
    p.add_argument("--metrics", type=str, default="reports/phase2_metrics.json")
    p.add_argument("--test-size", type=float, default=0.2)
    return p.parse_args()


def prepare_dirs(path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, header=None, names=["label", "text"], encoding="latin-1")
    return df


def train_and_eval(data_path: str, test_size: float = 0.2) -> dict:
    df = load_data(data_path)
    df = df.dropna(subset=["text", "label"]).reset_index(drop=True)
    df["label_num"] = df["label"].map({"ham": 0, "spam": 1})

    X = df["text"].astype(str).values
    y = df["label_num"].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)
    X_train_t = vectorizer.fit_transform(X_train)
    X_test_t = vectorizer.transform(X_test)

    clf = LogisticRegression(solver="liblinear", random_state=42, max_iter=1000)
    clf.fit(X_train_t, y_train)

    preds = clf.predict(X_test_t)
    probs = clf.predict_proba(X_test_t)[:, 1]

    acc = accuracy_score(y_test, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, preds, average="binary")
    cm = confusion_matrix(y_test, preds).tolist()
    roc_auc = float(roc_auc_score(y_test, probs))
    pr_auc = float(average_precision_score(y_test, probs))

    metrics = {
        "accuracy": float(acc),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
        "roc_auc": roc_auc,
        "pr_auc": pr_auc,
        "confusion_matrix": cm,
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
    }

    return {"model": clf, "vectorizer": vectorizer, "metrics": metrics}


def main() -> int:
    args = parse_args()
    data_path = os.path.abspath(args.data)

    if not os.path.exists(data_path):
        print(f"Data file not found: {data_path}")
        return 2

    result = train_and_eval(data_path, test_size=args.test_size)

    prepare_dirs(args.output_model)
    joblib.dump({"model": result["model"], "vectorizer": result["vectorizer"]}, args.output_model)
    print(f"Saved phase2 model to {args.output_model}")

    prepare_dirs(args.metrics)
    with open(args.metrics, "w", encoding="utf-8") as fh:
        json.dump(result["metrics"], fh, indent=2)
    print(f"Saved phase2 metrics to {args.metrics}")

    # If phase1 metrics exist, print a compact comparison
    phase1_metrics_path = os.path.join(os.path.dirname(args.metrics), "..", "phase1_metrics.json")
    phase1_metrics_path = os.path.normpath(phase1_metrics_path)
    if os.path.exists(phase1_metrics_path):
        try:
            with open(phase1_metrics_path, "r", encoding="utf-8") as fh:
                phase1 = json.load(fh)
            print("\nComparison (Phase1 SVM vs Phase2 LogisticRegression):")
            print(f"accuracy: {phase1.get('accuracy'):.4f} -> {result['metrics']['accuracy']:.4f}")
            print(f"precision: {phase1.get('precision'):.4f} -> {result['metrics']['precision']:.4f}")
            print(f"recall:    {phase1.get('recall'):.4f} -> {result['metrics']['recall']:.4f}")
            print(f"f1:        {phase1.get('f1'):.4f} -> {result['metrics']['f1']:.4f}")
            print(f"roc_auc:   {phase1.get('roc_auc', float('nan'))} -> {result['metrics']['roc_auc']:.4f}")
            print(f"pr_auc:    {phase1.get('pr_auc', float('nan'))} -> {result['metrics']['pr_auc']:.4f}")
        except Exception:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
