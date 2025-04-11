# --- pages/2_PT_Questions.py ---
import streamlit as st

st.set_page_config(page_title="Step 2 - PT", page_icon="💼", layout="centered")

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Step 2 of 6")
    def check_icon(key):
        return "✅" if key in st.session_state else "⬜️"

    st.markdown(f"{check_icon('user_info')} Step 1: Personal Info")
    st.markdown(f"{check_icon('PT1')} Step 2: Personality Traits")
    st.markdown(f"{check_icon('LP1')} Step 3: Learning Preferences")
    st.markdown(f"{check_icon('CS1')} Step 4: Cognitive Strengths")
    st.markdown(f"{check_icon('PS1')} Step 5: Professional Strengths")
    st.markdown(f"{check_icon('evaluation_rating')} Step 6: Evaluation")
    st.markdown(f"{check_icon('P1')} Step 7: Prediction")

    total = sum([
        'user_info' in st.session_state,
        'PT1' in st.session_state,
        'LP1' in st.session_state,
        'CS1' in st.session_state,
        'PS1' in st.session_state,
        'evaluation_rating' in st.session_state,
        'P1' in st.session_state
    ])
    st.progress(total / 7)

st.header("Section 1: Personality Traits")

st.markdown("""
<div style='text-align: justify'>
This section evaluates how individuals approach their work, make decisions, and interact with their professional environment. Understanding personality traits such as logical reasoning, collaboration, and adaptability is crucial in determining an individual's preferred work style and the types of roles they may excel in.
</div>
""", unsafe_allow_html=True)
# Add vertical space before the first slider
st.markdown("<br>", unsafe_allow_html=True)

# Define PT questions with descriptions
pt_questions = {
    "PT1": "I enjoy analyzing data and making logical decisions.",
    "PT2": "I prefer structured plans and organized processes over spontaneous decisions.",
    "PT3": "I am comfortable working in uncertain and dynamic environments.",
    "PT4": "I enjoy thinking of innovative and unconventional solutions to problems.",
    "PT5": "I thrive in collaborative settings and prefer working with people to achieve goals.",
    "PT6": "I feel most confident when making decisions based on factual data rather than intuition."
}

# Collect answers via sliders
pt_answers = {}
for key, question in pt_questions.items():
    pt_answers[key] = st.slider(f"{key}: {question}", 1, 5, 3)

# Navigation Buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/1_User_Info.py")

with col2:
    if st.button("Next →"):
        if 'answers' not in st.session_state:
            st.session_state['answers'] = {}
        st.session_state['answers'].update(pt_answers)
        st.switch_page("pages/3_Learning Preferences.py")