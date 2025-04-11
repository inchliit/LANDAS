# --- pages/4_CS_Questions.py ---
import streamlit as st

st.set_page_config(page_title="Section 4 - CS", page_icon="💼", layout="centered")

# ✅ Initialize answers if not yet done
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Section 4 of 6")
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

st.title("Section 4: Cognitive Strengths (CS)")

# ✅ Justified section description
st.markdown("""
<div style='text-align: justify'>
Cognitive strengths are critical in industrial engineering, where analytical thinking and problem-solving skills play a vital role. This section assesses abilities such as logical reasoning, pattern recognition, communication, and teamwork, all of which contribute to efficiency in various engineering roles.
</div>
""", unsafe_allow_html=True)

# ✅ Space before first question
st.markdown("<br>", unsafe_allow_html=True)

# CS questions
cs_questions = {
    "CS1": "I excel in solving mathematical and logical problems.",
    "CS2": "I am good at coordinating physical activities and hands-on tasks.",
    "CS3": "I communicate well and can easily collaborate with teams.",
    "CS4": "I prefer working independently and reflecting on ideas before making decisions.",
    "CS5": "I quickly identify inefficiencies in systems and processes.",
    "CS6": "I am skilled at recognizing patterns and trends in complex data."
}

# Slider collection
cs_answers = {}
for key, question in cs_questions.items():
    cs_answers[key] = st.slider(f"{key}: {question}", 1, 5, 3)

# ✅ Buttons for navigation
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/3_Learning Preferences.py")

with col2:
    if st.button("Next →"):
        if 'answers' not in st.session_state:
            st.session_state['answers'] = {}
        st.session_state['answers'].update(cs_answers)

        # ✅ Mark CS1 as complete at top-level for sidebar check
        st.session_state['CS1'] = cs_answers['CS1']

        st.switch_page("pages/5_Professional Strengths.py")
