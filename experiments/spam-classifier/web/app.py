import os
import json
from pathlib import Path
import joblib

try:
    import streamlit as st
except Exception:  # pragma: no cover - streamlit only required at runtime
    st = None


MODEL_REL_PATHS = [
    # Prefer bundled web model (for Streamlit deploy)
    os.path.join("models", "phase2_logreg.joblib"),
    os.path.join("models", "baseline_svm.joblib"),
    # Fallback to phase1 models
    os.path.join("..", "phase1", "models", "phase2_logreg.joblib"),
    os.path.join("..", "phase1", "models", "baseline_svm.joblib"),
]


def find_model_path() -> str | None:
    # Check web/ first (bundled), then experiments path relative to repo
    here = Path(__file__).parent
    for rel in MODEL_REL_PATHS:
        p = (here / rel).resolve()
        if p.exists():
            return str(p)
    # As a last resort, check repo-level experiments path
    alt = Path(__file__).parents[2] / "data"  # not used, placeholder
    return None


def load_model(model_path: str):
    data = joblib.load(model_path)
    # Expecting a dict with keys 'model' and 'vectorizer'
    if isinstance(data, dict) and "model" in data and "vectorizer" in data:
        return data["model"], data["vectorizer"]
    # Backwards compatibility: saved model directly
    return data, None


def predict_text(model, vectorizer, text: str) -> tuple[str, float]:
    x = [text]
    if vectorizer is not None:
        x_t = vectorizer.transform(x)
    else:
        # If no vectorizer, assume model accepts raw text (unlikely)
        x_t = x

    # Prefer predict_proba when available
    if hasattr(model, "predict_proba"):
        prob = float(model.predict_proba(x_t)[:, 1][0])
    elif hasattr(model, "decision_function"):
        # scale decision_function to (0,1) via sigmoid for display
        import math

        score = float(model.decision_function(x_t)[0])
        prob = 1 / (1 + math.exp(-score))
    else:
        prob = float(model.predict(x_t)[0])

    pred = model.predict(x_t)[0]
    label = "spam" if int(pred) == 1 else "ham"
    return label, prob


def load_dataset_stats():
    # Try to read the SMS dataset and return class distribution
    # Dataset is expected under experiments/spam-classifier/data/
    data_candidate = Path(__file__).parents[1] / "data" / "sms_spam_no_header.csv"
    if not data_candidate.exists():
        return None
    import pandas as pd

    df = pd.read_csv(data_candidate, header=None, names=["label", "text"], encoding="latin-1")
    dist = df[0].value_counts() if 0 in df.columns else df["label"].value_counts()
    return dist.to_dict()


def main():
    model_path = find_model_path()
    model = None
    vectorizer = None
    if model_path:
        try:
            model, vectorizer = load_model(model_path)
        except Exception as e:
            model = None
            vectorizer = None
            print("Failed to load model:", e)

    if st is None:
        print("Streamlit is not installed. Install streamlit to run the app: pip install streamlit")
        return

    st.title("Spam classifier demo")
    st.markdown("Enter a message (SMS or email) and click Predict to see the model output.")

    sample = st.text_area("Message text", value="Congratulations! You have won a prize. Call now to claim.")
    if st.button("Predict"):
        if model is None:
            st.error("No model available. Ensure the model artifact is present in the web or phase1 models directory.")
        else:
            label, prob = predict_text(model, vectorizer, sample)
            st.write(f"Prediction: **{label.upper()}**")
            st.write(f"Confidence (approx): **{prob:.3f}**")

    st.sidebar.header("Dataset stats")
    stats = load_dataset_stats()
    if stats:
        st.sidebar.write(json.dumps(stats, indent=2))
    else:
        st.sidebar.write("Dataset not found in expected path.")


if __name__ == "__main__":
    main()
