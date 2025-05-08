# --- pages/8_Post_Result_Survey.py ---
import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import base64

st.set_page_config(page_title="Section 8 - Post Result Survey", page_icon="📝", layout="centered")

st.title("📋 Quick Post-Result Survey")

st.markdown("""
Thank you for completing the career assessment. Please answer the following before downloading your results.
""")

# Radio buttons
satisfied = st.radio("1. Are you satisfied with your result?", ["Yes", "No"], horizontal=True)
expected = st.radio("2. Was this what you expected?", ["Yes", "No"], horizontal=True)
interested = st.radio("3. Would you consider pursuing your top recommended role?", ["Yes", "No"], horizontal=True)
comment = st.text_area("Any feedback or suggestions? (Optional)")

# Save to Google Sheet
def save_post_feedback():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["GOOGLE_CREDENTIALS"], scope)
    client = gspread.authorize(creds)
    sheet = client.open("LANDAS_Responses").worksheet("PostSurvey")
    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        st.session_state.get("user_info", {}).get("email", ""),
        satisfied, expected, interested, comment
    ]
    sheet.append_row(row)


# --- Optional: Download Feature ---
st.markdown("---")
st.subheader("⬇️ Export Your Results")

export_df = pd.DataFrame([{
    "Name": user_info["name"],
    "Email": user_info["email"],
    "University": user_info["university"],
    "Top Choice": top3_jobs[0],
    "Confidence 1": f"{probs[top3_indices[0]] * 100:.2f}%",
    "Second Choice": top3_jobs[1],
    "Confidence 2": f"{probs[top3_indices[1]] * 100:.2f}%",
    "Third Choice": top3_jobs[2],
    "Confidence 3": f"{probs[top3_indices[2]] * 100:.2f}%"
}])

csv = export_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download My Results as CSV",
    data=csv,
    file_name='LANDAS_Results.csv',
    mime='text/csv',
)