# Data Analysis and Applications — HW3

This repository contains the homework project for Data Analysis and Applications (HW3). It uses an OpenSpec-driven workflow and includes a spam-classifier experiment with multiple phases plus a minimal Streamlit demo.

Overview
- `openspec/` — OpenSpec proposals, specs, and project conventions. Use this to plan and review changes.
- `experiments/spam-classifier/` — experiment code and demo for the spam classifier.
  - `phase1/` — baseline experiment (data fetch, SVM baseline, Phase 2 logistic regression model and reports).
  - `web/` — minimal Streamlit demo app that loads the Phase 2 model by default.

Quickstart (PowerShell)

1) Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies for experiments

```powershell
pip install -r experiments\spam-classifier\phase1\requirements.txt
```

3) Download the dataset (Phase 1)

```powershell
python experiments\spam-classifier\phase1\scripts\fetch_data.py
```

4) Train baseline (SVM) — Phase 1

```powershell
python experiments\spam-classifier\phase1\scripts\train_baseline.py --data experiments\spam-classifier\data\sms_spam_no_header.csv
```

5) Train logistic regression — Phase 2

```powershell
python experiments\spam-classifier\phase1\scripts\train_phase2.py --data experiments\spam-classifier\data\sms_spam_no_header.csv
```

Run the Streamlit demo locally

```powershell
pip install -r experiments\spam-classifier\web\requirements.txt
streamlit run experiments\spam-classifier\web\app.py
```

Notes about the web demo
- The demo attempts to load the Phase 2 model from `experiments/spam-classifier/phase1/models/phase2_logreg.joblib`. A bundled copy is available at `experiments/spam-classifier/web/models/phase2_logreg.joblib` for easy deployment to Streamlit Cloud.
- For production use, prefer external object storage for model artifacts rather than committing binaries to the repo.

OpenSpec and contributing
- Proposals and change deltas live in `openspec/changes/`. Follow the OpenSpec conventions in `openspec/AGENTS.md` when creating proposals.
- Typical file locations for changes:
  - `openspec/changes/<change-id>/proposal.md`
  - `openspec/changes/<change-id>/tasks.md`
  - `openspec/changes/<change-id>/specs/<capability>/spec.md`

Repository pushed to GitHub
- This repository has been pushed to: https://github.com/davidkuo3/Data-Analysis-and-Applications-hw3.git

If you want any of the following done next, tell me:
- Add a GitHub Actions CI workflow to run smoke tests on PRs
- Remove the bundled model and switch the demo to download the model from external storage
- Improve the Streamlit UI to match the provided reference more closely
