# --- pages/5_Evaluation.py ---
import streamlit as st

st.set_page_config(page_title="Section 5 - Evaluation", page_icon="💼", layout="centered")

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Section 5 of 6")
    st.sidebar.progress(5 / 6)

st.title("⭐️ Quick Evaluation")

st.markdown("""
<div style='text-align: justify'>
We'd love to hear your thoughts on this assessment experience before we reveal your top career path matches.
Please rate your experience below:
</div>
""", unsafe_allow_html=True)

# Star rating (1–5)
rating = st.slider("How would you rate your experience?", 1, 5, 4, format="%d ⭐")

st.text_area("Any feedback or suggestions?", key="feedback")

# Navigation
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/5_Professional Strengthspy")

with col2:
    if st.button("See My Career Path →"):
        st.session_state['evaluation_rating'] = rating
        st.switch_page("pages/7_Job_Prediction.py")
