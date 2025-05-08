import streamlit as st

st.set_page_config(page_title="Admin Dashboard", page_icon="📊", layout="wide")

# --- Admin Authentication ---
def check_access():
    if "admin_auth" not in st.session_state:
        st.session_state["admin_auth"] = False

    if not st.session_state["admin_auth"]:
        password = st.text_input("🔐 Enter Admin Password", type="password")
        if password == "alphaadmin2024":  # ✅ Replace with your secret pass
            st.session_state["admin_auth"] = True
            st.success("✅ Access granted.")
        else:
            st.warning("Incorrect password." if password else "")
        st.stop()

check_access()

# --- Embedded GSheet Dashboard ---
st.title("📊 LANDAS Admin Dashboard")

st.markdown("> 👇 Below is the live dashboard from the LANDAS Google Sheet.")

dashboard_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQdzYcdoi3txtJboomaUfqWErNf3IaqxYklomTUOeQ0za_IEpzrWI6XJWiSe8MW9I60-nbWfx9__Wvc/pubhtml?gid=2043121298&single=true"  # replace with your published link

st.components.v1.iframe(dashboard_url, height=1000, scrolling=True)
