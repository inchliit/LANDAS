# --- pages/5_Evaluation.py ---
import streamlit as st

st.set_page_config(page_title="Section 5 - Evaluation", page_icon="💼", layout="centered")

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Section 5 of 6")
    def check_icon(key):
        return "✅" if key in st.session_state else "⬜️"

    st.markdown(f"{check_icon('user_info')} Step 1: Personal Info")
    st.markdown(f"{check_icon('PT1')} Step 2: Personality Traits")
    st.markdown(f"{check_icon('LP1')} Step 3: Learning Preferences")
    st.markdown(f"{check_icon('CS1')} Step 4: Cognitive Strengths")
    st.markdown(f"{check_icon('PS1')} Step 5: Professional Strengths")
    st.markdown(f"{check_icon('evaluation_rating')} Step 6: Evaluation")
    st.markdown(f"{check_icon('evaluation_rating')} Step 7: Prediction")

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

st.title("⭐️ Quick Evaluation")

st.markdown("""
<div style='text-align: justify'>
We'd love to hear your thoughts on this assessment experience before we reveal your top career path matches.
Please rate your experience below:
</div>
""", unsafe_allow_html=True)

# Star rating (1–5)
rating = st.slider("How would you rate your experience?", 1, 5, 1, format="%d ⭐")

# Text input for feedback
feedback = st.text_area("Any feedback or suggestions?")

# Navigation
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/5_Professional Strengths.py")

with col2:
    if st.button("See My Career Path →"):
        st.session_state['evaluation_rating'] = rating
        st.session_state['feedback'] = feedback  # ✅ this is key
        st.switch_page("pages/7_Job_Prediction.py")