## ADDED Requirements

### Requirement: Demo web UI for spam-classifier
The project SHALL provide a demo web application that allows users to input an email or SMS message and receive a spam/ham prediction along with a confidence score. The web UI SHALL be deployable to Streamlit Cloud.

#### Scenario: Local run
- **WHEN** a developer runs `streamlit run app.py` from `experiments/spam-classifier/web/`
- **THEN** the application starts and displays an input field for message text
- **AND** the application returns a predicted label and confidence score for sample inputs

#### Scenario: Streamlit Cloud deployment
- **WHEN** the repository is connected to Streamlit Cloud and the app is configured to use `experiments/spam-classifier/web/app.py`
- **THEN** Streamlit Cloud builds and deploys the app successfully
- **AND** the app loads the model artifact (either bundled or downloaded at startup) and accepts user input in the browser

#### Scenario: Smoke test
- **WHEN** the smoke test runs (local import or CI job)
- **THEN** it imports the app module and calls the internal prediction function with a sample message and receives a label and probability
