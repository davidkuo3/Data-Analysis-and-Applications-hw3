## Why

Users and stakeholders benefit from an interactive demo that showcases the spam-classifier model in action. A simple web UI makes it easier to evaluate model behavior on real inputs, collect feedback, and demonstrate deployment readiness. The reference implementation (https://github.com/huanchen1107/2025ML-spamEmail.git) provides a compact Streamlit-based layout to emulate.

## What Changes

- Create a demo web application that exposes the Phase 1/Phase 2 models (and future improvements) through a Streamlit UI. The app SHALL accept user input (email/SMS text), show predictions and probability/confidence scores, and display example dataset statistics.
- Provide a production-ready repository layout for the demo and configure it for deployment to Streamlit Cloud (include `requirements.txt`, `streamlit` entrypoint, `README.md`, and instructions for connecting the app to the trained model artifact stored in the repo or loaded at startup).
- Use the referenced repo (https://github.com/huanchen1107/2025ML-spamEmail.git) as a visual and structural guide but adapt for this project's model artifacts and evaluation results.

**Change id:** `add-spam-classifier-demo-site`

## Impact

- New files and directories: `experiments/spam-classifier/web/` (Streamlit app), updated `README.md` with deployment instructions, and CI or small automation to package the model artifact for Streamlit.
- Affected capabilities: UI/demo capability (new) and experiment reproducibility (linking artifacts to the demo).
- Dependencies: `streamlit` and any web-specific python dependencies (keep minimal). The demo will rely on the model artifact produced in Phase 1/2 and the vectorizer for text processing.

## Deliverables

1. `experiments/spam-classifier/web/` containing:
   - `app.py` — Streamlit application that loads the model+vectorizer and serves predictions
   - `requirements.txt` — minimal packages for Streamlit Cloud
   - `README.md` — deployment and usage instructions
   - optional: `Procfile` or `.streamlit/config.toml` if needed
2. Deployment: a GitHub repository branch ready to connect to Streamlit Cloud and a deployed URL (Streamlit Cloud app) demonstrating live predictions.
3. Acceptance artifacts: link to deployed app, screenshots, and an automated smoke test that verifies the app loads and returns a prediction for a sample input.

## Acceptance Criteria

- The app runs locally with `streamlit run app.py` and accepts text input, returning a predicted label and confidence score.
- The app is deployable to Streamlit Cloud; after connecting the repository, the app launches and loads the model artifact without manual intervention.
- Documentation: `README.md` contains clear Streamlit Cloud deployment steps and how to update the model artifact.
- A basic smoke test script `tests/smoke_test_app.py` or a GitHub Action is included that checks the app endpoint (if deployed) or runs a headless launch to ensure `app.py` imports and returns a prediction.

## Migration

- This is additive. Add a `web/` folder under `experiments/spam-classifier/` and update the project README to include deployment instructions. No existing specs are removed.

## Non-goals

- This change does not include advanced authentication, multi-tenant deployment, or production-grade scaling. Streamlit Cloud demo is intended for interactive demonstration and light usage only.

## Reference

- Reference project to emulate: https://github.com/huanchen1107/2025ML-spamEmail.git

---
If you approve, I will scaffold the Streamlit app files (minimal `app.py`, `requirements.txt`, and a smoke test), wire the Phase 2 model (logistic regression) into the demo, and provide deployment instructions for Streamlit Cloud.
