## Why

Spam classification is a common NLP classification problem with clear ML baselines and evaluation metrics. The goal of this change is to create a reproducible project scaffold for a spam-classifier experiment that culminates in a logistic regression model for spam detection. This will provide a clear, teachable pipeline for data ingestion, preprocessing, model training, evaluation, and artifacts for later phases (improvements, deployment, monitoring).

Note: the initial dataset linked by the request is an SMS spam dataset (CSV). I will treat it as an appropriate baseline dataset for Phase 1, but the final project can substitute an email-specific dataset later if desired.

## What Changes

- Add a new capability / change: `add-spam-classifier` that documents and scaffolds a multi-phase spam-classifier project.
- Phase 1 (baseline): ingest the provided CSV dataset, run preprocessing, train a baseline SVM classifier, and produce baseline metrics and artifacts (trained model file, evaluation report, and a reproducible script or notebook).
- Later phases (placeholders) will include model selection (logistic regression and tuning), dataset expansion (email-specific datasets), and deployment experiments.

**Change id:** `add-spam-classifier`

## Impact

- Affected files (new): `openspec/changes/add-spam-classifier/proposal.md`, plus subsequent `tasks.md`, `specs/` deltas, and implementation scripts/notebooks under a new `experiments/spam-classifier/` directory.
- Affected capabilities: new capability for ML experiment scaffolding and reproducible baseline training.
- Expected infra: local Python environment (recommended: venv or conda), typical ML packages (scikit-learn, pandas, numpy), and optional Jupyter for notebooks.

## Phase 1 — Setup Baseline

1. Name: phase1-setup-baseline
2. Goal: Build a basic baseline SVM classifier and produce reproducible results using the provided dataset.
3. Data source: https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv
   - Note: this is an SMS spam dataset (two columns: label, text). If you prefer an email dataset, supply the URL or file and I will swap it.
4. Deliverables:
   - `experiments/spam-classifier/phase1/` containing:
     - `data-fetch.ipynb` or `scripts/fetch_data.py` that downloads and saves the CSV locally
     - `notebooks/phase1-baseline.ipynb` demonstrating preprocessing, feature extraction (e.g., TF-IDF), model training (SVM), and evaluation
     - `scripts/train_baseline.py` (reproducible CLI script) that saves model artifact `models/baseline_svm.pkl` and a JSON metrics report `reports/phase1_metrics.json`
     - `README.md` with quick run instructions and environment setup
   - Evaluation metrics: confusion matrix, accuracy, precision, recall, F1, and per-class support

## Acceptance Criteria

- The baseline pipeline can be run end-to-end by executing a single script or notebook and produces a saved model and a metrics report.
- The dataset is downloaded from the given URL and saved to `data/` within the experiment folder.
- Results (metrics) and the training artifacts are checked into the `experiments/spam-classifier/phase1/` folder (or a CI artifact store) for review.
- Reproducibility: a `requirements.txt` or `environment.yml` is included and the script runs on a standard Python 3.8+ environment.

## Subsequent phases (placeholders)

- Phase 2: Model selection and tuning (logistic regression, hyperparameter search)
- Phase 3: Dataset expansion (email-specific datasets), cross-domain evaluation
- Phase 4: Deployment experiment (packaging model as a simple HTTP inference service)

These phase entries are intentionally left as placeholders and will be expanded when Phase 1 completes and we have evaluation results.

## Migration

- This change is additive. No migration required for existing specs. Implementation will add new directories and may add CI steps to validate experiment reproducibility.

## Non-goals

- This change does not include production-grade deployment or automatic ingestion pipelines for streaming email. It focuses on a research/experiment scaffold and reproducible baseline.

## Notes and assumptions

- The requester wrote "spam email classification" but provided an SMS dataset link. Assumption: SMS dataset is acceptable for Phase 1 baseline; later phases can use email-specific data.
- The requester specified logistic regression as the target technique; Phase 1 will use SVM as an explicit baseline per the plan. Phase 2 will add logistic regression and hyperparameter tuning.
- Recommended stack: Python 3.8+, pandas, scikit-learn, joblib (for model serialization), and optionally Jupyter.

---
Create `tasks.md` and spec deltas next to this proposal when you want me to scaffold tasks and spec changes. If you'd like, I can also scaffold the Phase 1 scripts/notebook and `requirements.txt` now.
