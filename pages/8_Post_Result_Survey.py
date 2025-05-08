# --- pages/8_Post_Result_Survey.py ---
import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

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

# Final submit button triggers save
if st.button("✅ Submit Feedback"):
    save_post_feedback()
    st.success("✅ Thank you for your response! Your feedback has been recorded.")

if st.button("🏠 Back to Homepage"):
        st.switch_page("LANDAS.py")
