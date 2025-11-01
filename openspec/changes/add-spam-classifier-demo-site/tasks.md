## 1. Implementation

- [ ] 1.1 Create `experiments/spam-classifier/web/app.py` — a Streamlit app that loads the trained model and vectorizer and serves predictions.
- [ ] 1.2 Add `experiments/spam-classifier/web/requirements.txt` with pinned dependencies (`streamlit`, `scikit-learn`, `joblib`, `pandas`).
- [ ] 1.3 Add `README.md` with Streamlit Cloud deployment instructions and environment notes.
- [ ] 1.4 Add a small smoke test (`tests/smoke_test_app.py`) that validates the app imports and a sample prediction.
- [ ] 1.5 Add model-loading logic: app loads `phase2_logreg.joblib` by default, with fallback to a bundled model if needed.
- [ ] 1.6 Verify locally: `streamlit run app.py` works and displays the demo UI.

## 2. CI / Deployment

- [ ] 2.1 Optionally add a GitHub Actions workflow to run tests and optionally push a tag.
- [ ] 2.2 Document how to link the GitHub repository to Streamlit Cloud and set required env vars.

## 3. Acceptance

- [ ] 3.1 Deployed Streamlit link provided and verified (manual check or automated smoke test).
- [ ] 3.2 README contains a small section on updating the model artifact and redeploying.
