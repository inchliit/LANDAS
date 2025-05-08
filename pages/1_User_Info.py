import streamlit as st

st.set_page_config(page_title="Step 1 - User Info", page_icon="💼", layout="centered")

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Step 1 of 6")
    def check_icon(key):
        return "✅" if key in st.session_state else "⬜️"

    st.markdown(f"{check_icon('user_info')} Section 1: Personal Info")
    st.markdown(f"{check_icon('PT1')} Section 2: Personality Traits")
    st.markdown(f"{check_icon('LP1')} Section 3: Learning Preferences")
    st.markdown(f"{check_icon('CS1')} Section 4: Cognitive Strengths")
    st.markdown(f"{check_icon('PS1')} Section 5: Professional Strengths")
    st.markdown(f"{check_icon('evaluation_rating')} Section 6: Evaluation")
    st.markdown(f"{check_icon('P1')} Section 7: Prediction")

    total = sum([
        'user_info' in st.session_state,
        'PT1' in st.session_state,
        'LP1' in st.session_state,
        'CS1' in st.session_state,
        'PS1' in st.session_state,
        'evaluation_rating' in st.session_state,
        'P1' in st.session_state
    ])
    st.progress(total / 8)

st.title("Section 1: Personal Information")

# Personal info
col1, col2 = st.columns(2)
first_name = col1.text_input("First Name")
last_name = col2.text_input("Last Name")
email = st.text_input("Email")
university = st.text_input("University/College Name")
goals = st.text_area("Describe your career goals")

st.markdown("## 🧾 Demographic Info for Prediction")
age_input = st.text_input("Age (18–60)", "").strip()
if age_input.isdigit() and 18 <= int(age_input) <= 60:
    age = int(age_input)
else:
    age = None
gender = st.selectbox("Gender", ["", "Male", "Female", "Other"])
education = st.selectbox("Education", ["", "Bachelor's Degree", "Masteral's Degree", "Doctorate Degree"])

# --- Navigation Buttons ---
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/1_Ops_Manual.py")

with col2:
    if st.button("Next →"):
        # Validate required fields
        if not first_name or not last_name or not email:
            st.warning("⚠️ Please complete your full name and email address.")
        elif "@" not in email or "." not in email:
            st.warning("⚠️ Please enter a valid email address.")
        elif gender == "" or education == "" or age is None:
            st.warning("⚠️ Please complete all demographic information, including a valid age (18–60).")

        else:
            st.session_state['user_info'] = {
                'name': f"{first_name.strip().title()} {last_name.strip().title()}",
                'email': email.strip(),
                'university': university.strip(),
                'goals': goals.strip()
            }
            st.session_state['demographics'] = {
                'Age': age,
                'Gender': gender,
                'EDUCATION': education
            }
            st.success("✅ Information saved successfully!")
            st.switch_page("pages/2_Personality Traits.py")
