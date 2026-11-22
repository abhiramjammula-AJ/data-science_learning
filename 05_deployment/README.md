# Model Deployment with Streamlit

A logistic regression model, trained on `claimants.csv`, served as a small web app with [Streamlit](https://streamlit.io/). The user enters claimant details in the sidebar, and the app predicts whether the claimant hires an attorney.

## Files

| File | Purpose |
| --- | --- |
| `claimants_logistic_app.py` | Streamlit app: trains the model and shows predictions |
| `claimants.csv` | Training data |

## Run it

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

# 2. Install dependencies
pip install streamlit pandas scikit-learn

# 3. Launch the app from this folder
cd 05_deployment
streamlit run claimants_logistic_app.py
```

Streamlit opens the app in your browser at `http://localhost:8501`. Press `Ctrl + C` in the terminal to stop it.

> To check the install first, run `streamlit hello` to open Streamlit's demo app.
