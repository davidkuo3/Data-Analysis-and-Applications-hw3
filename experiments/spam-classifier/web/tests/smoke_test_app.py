"""Simple smoke test for the Streamlit app's prediction function.

This test imports the app and calls the predict_text function. It does not run Streamlit UI.
"""
import os
import sys

# Ensure repo root is on path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

from web import app


def test_predict():
    # Attempt to find a model; test will skip if no model is present
    model_path = app.find_model_path()
    if not model_path:
        print("No model found for smoke test; skipping")
        return
    model, vectorizer = app.load_model(model_path)
    label, prob = app.predict_text(model, vectorizer, "Free entry: claim your prize now")
    assert label in ("spam", "ham")
    assert isinstance(prob, float)


if __name__ == "__main__":
    test_predict()
    print("smoke test completed")
