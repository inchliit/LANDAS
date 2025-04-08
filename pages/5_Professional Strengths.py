# --- pages/5_PS_Questions.py ---
import streamlit as st

st.set_page_config(page_title="Section 5 - PS", page_icon="💼", layout="centered")

# ✅ Ensure answers state is initialized
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Section 5 of 6")
    st.sidebar.progress(5 / 6)

st.title("Section 5: Professional Strengths (PS)")

# ✅ Justified description
st.markdown("""
<div style='text-align: justify'>
This section measures work-related strengths, leadership potential, and professional behavior in industrial engineering settings. Attributes such as initiative, attention to detail, multitasking, and leadership skills help determine which professionals are best suited for managerial or specialized technical roles.
</div>
""", unsafe_allow_html=True)

# ✅ Space before first slider
st.markdown("<br>", unsafe_allow_html=True)

# ✅ Full question text
ps_questions = {
    "PS1": "I take initiative in starting projects and seeing them through to completion.",
    "PS2": "I find it rewarding to help others develop their skills and knowledge.",
    "PS3": "I am quick to adapt to new situations and enjoy working in dynamic environments.",
    "PS4": "I am highly detail-oriented and ensure accuracy in all aspects of my work.",
    "PS5": "I am skilled in managing multiple tasks and meeting deadlines efficiently.",
    "PS6": "I enjoy leading teams, making strategic decisions, and improving systems."
}

# ✅ Capture answers
ps_answers = {}
for key, question in ps_questions.items():
    ps_answers[key] = st.slider(f"{key}: {question}", 1, 5, 3)

# ✅ Navigation buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/4_Cognitive Strengths.py")
with col2:
    if st.button("Next →"):
        st.session_state['answers'].update(ps_answers)
        st.switch_page("pages/6_Evaluation.py")
