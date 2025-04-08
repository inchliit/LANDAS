import streamlit as st

st.set_page_config(page_title="Step 1 - User Info", page_icon="💼", layout="centered")

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Step 1 of 6")
    st.sidebar.progress(1/6)

st.title("Step 1: Personal Information")

# Personal info
col1, col2 = st.columns(2)
first_name = col1.text_input("First Name")
last_name = col2.text_input("Last Name")
email = st.text_input("Email")
university = st.text_input("University/College Name")
goals = st.text_area("Describe your career goals")

st.markdown("## 🧾 Demographic Info for Prediction")

age = st.slider("Age", 18, 60, 25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
education = st.selectbox("Education", ["Bachelor's Degree", "Masteral's Degree", "Doctorate Degree"])

# --- Navigation Buttons ---
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("streamlit_app.py")

with col2:
    if st.button("Next →"):
        # Store all user info
        st.session_state['user_info'] = {
            'name': f"{first_name} {last_name}",
            'email': email,
            'university': university,
            'goals': goals
        }
        # Store demographic variables for prediction
        st.session_state['demographics'] = {
            'Age': age,
            'Gender': gender,
            'EDUCATION': education,
        }
        st.switch_page("pages/2_Personality Traits.py")
