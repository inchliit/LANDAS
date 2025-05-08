import streamlit as st

st.set_page_config(page_title="Admin Dashboard", page_icon="📊", layout="wide")

# --- Admin Authentication ---
def check_access():
    if "admin_auth" not in st.session_state:
        st.session_state["admin_auth"] = False

    if not st.session_state["admin_auth"]:
        st.title("🔐 Admin Access")
        password = st.text_input("Enter Admin Password", type="password")
        if password == "alphaadmin2024":
            st.session_state["admin_auth"] = True
            st.success("✅ Access granted.")
            st.rerun()  # ✅ rerun the app with new session state
        else:
            if password:  # only show warning after input
                st.warning("❌ Incorrect password.")
        st.stop()

check_access()

# --- Embedded GSheet Dashboard ---
st.title("📊 LANDAS Admin Dashboard")
st.markdown("> 👇 Below is the live dashboard from the LANDAS Google Sheet.")

dashboard_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQdzYcdoi3txtJboomaUfqWErNf3IaqxYklomTUOeQ0za_IEpzrWI6XJWiSe8MW9I60-nbWfx9__Wvc/pubhtml?gid=2043121298&single=true"
st.components.v1.iframe(dashboard_url, height=1000, scrolling=True)