# --- pages/9_Admin_Dashboard.py --- or similar
import streamlit as st

st.set_page_config(page_title="Admin Dashboard", page_icon="📊", layout="wide")

# --- Admin Authentication ---
def check_access():
    if "admin_auth" not in st.session_state:
        st.session_state["admin_auth"] = False

    if not st.session_state["admin_auth"]:
        password = st.text_input("🔐 Enter Admin Password", type="password")
        if password == "alphaadmin2024":
            st.session_state["admin_auth"] = True
            st.success("✅ Access granted.")
            st.experimental_rerun()  # 👈 reruns the app to render the dashboard
        else:
            st.warning("Incorrect password." if password else "")
            st.stop()

check_access()

# --- Admin Dashboard Display ---
st.title("📊 LANDAS Admin Dashboard")
st.markdown("> ✅ Live dashboard pulled from Google Sheets")

# Embed Published GSheet (make sure it's 'Published to Web')
dashboard_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQdzYcdoi3txtJboomaUfqWErNf3IaqxYklomTUOeQ0za_IEpzrWI6XJWiSe8MW9I60-nbWfx9__Wvc/pubhtml?gid=2043121298&single=true"

st.components.v1.iframe(dashboard_url, height=1000, scrolling=True)