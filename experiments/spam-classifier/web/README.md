# Spam Classifier Demo (Streamlit)

This is a minimal Streamlit demo that loads the Phase 2 logistic regression model and provides a simple UI for trying text inputs.

Run locally

```powershell
# create venv and activate (PowerShell)
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r experiments\spam-classifier\web\requirements.txt
streamlit run experiments\spam-classifier\web\app.py
```

Model artifact

- By default the app attempts to load `experiments/spam-classifier/phase1/models/phase2_logreg.joblib`.
- For easiest deployment, copy the model into the web folder (e.g., `experiments/spam-classifier/web/models/phase2_logreg.joblib`) so Streamlit Cloud can access it at build/deploy time.

Deploy to Streamlit Cloud

1. Push this repository to GitHub (or use the repo root).
2. Ensure `experiments/spam-classifier/web/requirements.txt` lists required packages.
3. In Streamlit Cloud, create a new app and point the app file to `experiments/spam-classifier/web/app.py`.
4. Optionally bundle `models/phase2_logreg.joblib` into `experiments/spam-classifier/web/models/` before pushing to simplify model access.

Notes

- This demo is intentionally minimal. For production or public deployment, avoid committing large model artifacts to the repo; consider using an external object storage and load model at startup.
