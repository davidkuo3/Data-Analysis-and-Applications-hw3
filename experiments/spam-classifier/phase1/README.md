# Spam classifier — Phase 1 (baseline)

This folder contains a reproducible baseline experiment for spam classification (SMS dataset).

Requirements
- Python 3.8+
- Create a virtual environment and install dependencies:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

Quick steps
1. Download dataset

```powershell
python scripts\fetch_data.py
```

2. Train baseline SVM model

```powershell
python scripts\train_baseline.py --data data\sms_spam_no_header.csv
```

Artifacts
- `models/baseline_svm.joblib` — saved model + vectorizer
- `reports/phase1_metrics.json` — evaluation metrics

Notes
- Phase 1 uses a LinearSVC baseline. Phase 2 will add logistic regression and hyperparameter tuning per the proposal.
