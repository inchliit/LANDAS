# --- pages/7_Job_Prediction.py ---
import streamlit as st
import pandas as pd
import joblib
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- Page Config ---
st.set_page_config(page_title="Section 7 - Prediction", page_icon="💼", layout="centered")

# --- Sidebar ---
with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Section 7 of 7")
    st.sidebar.progress(7 / 7)

st.title("🔮 Your Career Path Recommendations")

# --- Load model, encoders, and feature order ---
model = joblib.load("job_predictor_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

with open("feature_names.txt", "r") as f:
    expected_features = [line.strip() for line in f.readlines()]

# --- Load user inputs from previous steps ---
if 'answers' in st.session_state and 'demographics' in st.session_state and 'user_info' in st.session_state:
    demo = st.session_state['demographics']
    answers = st.session_state['answers']
    user_info = st.session_state['user_info']

    # Prepare input for prediction
    input_df = pd.DataFrame([{
        "Age": demo["Age"],
        "Gender": label_encoders["Gender"].transform([demo["Gender"]])[0],
        "EDUCATION": label_encoders["EDUCATION"].transform([demo["EDUCATION"]])[0],
        **answers
    }])
    input_df = input_df[expected_features]  # reorder columns

    # --- Prediction Logic ---
    probs = model.predict_proba(input_df)[0]
    top3_indices = probs.argsort()[-3:][::-1]
    top3_jobs = label_encoders["JOB"].inverse_transform(top3_indices)

    st.subheader("🔝 Top 3 Career Path Matches")
    for i, idx in enumerate(top3_indices):
        job_title = top3_jobs[i]
        confidence = probs[idx] * 100
        st.markdown(f"### {i+1}. **{job_title}**")
        if job_title in job_assets:
            st.image(job_assets[job_title]["image"], width=200)
            st.markdown(f"_{job_assets[job_title]['desc']}_")

    # --- Save to Google Sheet ---
    def save_to_gsheet(data):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("LANDAS_Responses").worksheet("Responses")

        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["Name"],
            data["Email"],
            data["University"],
            data["Goals"],
            data["Age"],
            data["Gender"],
            data["EDUCATION"],
            *[data.get(f"PT{i}", "") for i in range(1, 7)],
            *[data.get(f"LP{i}", "") for i in range(1, 7)],
            *[data.get(f"CS{i}", "") for i in range(1, 7)],
            *[data.get(f"PS{i}", "") for i in range(1, 7)],
            data["P1"], data["C1"],
            data["P2"], data["C2"],
            data["P3"], data["C3"]
        ]
        sheet.append_row(row)

    # --- Structure data for saving ---
    full_data = {
        "Name": user_info["name"],
        "Email": user_info["email"],
        "University": user_info["university"],
        "Goals": user_info["goals"],
        "Age": demo["Age"],
        "Gender": demo["Gender"],
        "EDUCATION": demo["EDUCATION"],
        **answers,
        "P1": top3_jobs[0],
        "C1": f"{probs[top3_indices[0]] * 100:.2f}%",
        "P2": top3_jobs[1],
        "C2": f"{probs[top3_indices[1]] * 100:.2f}%",
        "P3": top3_jobs[2],
        "C3": f"{probs[top3_indices[2]] * 100:.2f}%"
    }

    try:
        save_to_gsheet(full_data)
        st.success("✅ Your results have been saved successfully to Google Sheets!")
    except Exception as e:
        st.error(f"❌ Error saving to Google Sheets: {e}")

else:
    st.error("Please complete all steps before this page.")
