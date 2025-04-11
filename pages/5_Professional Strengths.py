# --- pages/5_PS_Questions.py ---
import streamlit as st

st.set_page_config(page_title="Section 5 - PS", page_icon="💼", layout="centered")

# ✅ Ensure answers state is initialized
if 'answers' not in st.session_state:
    st.session_state['answers'] = {}

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

st.title("Section 5: Professional Strengths (PS)")

# ✅ Justified description
st.markdown("""
<div style='text-align: justify'>
This section measures work-related strengths, leadership potential, and professional behavior in industrial engineering settings. Attributes such as initiative, attention to detail, multitasking, and leadership skills help determine which professionals are best suited for managerial or specialized technical roles.
</div>
""", unsafe_allow_html=True)

# Show the Likert Scale reference image
st.image("assets/Likert_Scale.png", use_container_width=True)

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

# --- Custom CSS to increase slider number font size ---
st.markdown("""
<style>
.css-1emrehy.edgvbvh3 {   /* numeric label */
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

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
        if 'answers' not in st.session_state:
            st.session_state['answers'] = {}
        st.session_state['answers'].update(ps_answers)
        # ✅ Mark PS1 as complete at top-level for sidebar check
        st.session_state['PS1'] = ps_answers['PS1']
        st.switch_page("pages/6_Evaluation.py")
