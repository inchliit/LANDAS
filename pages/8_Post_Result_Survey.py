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

# Final submit button triggers save + download
if st.button("✅ Submit and Download"):
    save_post_feedback()

    # Prepare CSV for download
    export_df = pd.DataFrame([{
        "Name": st.session_state["user_info"]["name"],
        "Email": st.session_state["user_info"]["email"],
        "University": st.session_state["user_info"]["university"],
        "Top Choice": st.session_state["P1"],
        "Confidence": st.session_state["C1"],
        "Second Choice": st.session_state["P2"],
        "Third Choice": st.session_state["P3"],
    }])
    csv = export_df.to_csv(index=False).encode("utf-8")

    # Auto-download link
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="LANDAS_Results.csv">📥 Click here if download didn\'t start automatically</a>'
    st.markdown("✅ Submitted! Your download should start now.", unsafe_allow_html=True)
    st.markdown(href, unsafe_allow_html=True)
