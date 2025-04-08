# --- pages/3_LP_Questions.py ---
import streamlit as st

st.set_page_config(page_title="Step 3 - LP", page_icon="💼", layout="centered")

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Step 3 of 6")
    st.sidebar.progress(3 / 6)

st.title("Section 3: Learning Preferences (LP)")

st.markdown("""
<div style='text-align: justify'>
The Learning Preferences section explores the ways in which individuals acquire and retain knowledge. Since industrial engineering roles require continuous learning, this section helps identify whether professionals prefer hands-on experiences, visual materials, reading, discussions, or technology-driven learning, aiding in recommending roles that match their learning styles.
</div>
""", unsafe_allow_html=True)

# Add vertical space before the first slider
st.markdown("<br>", unsafe_allow_html=True)

# LP questions
lp_questions = {
    "LP1": "I learn best through hands-on activities and practical applications.",
    "LP2": "I grasp concepts better when I see diagrams, charts, or visual presentations.",
    "LP3": "I prefer reading and writing detailed notes to fully understand technical information.",
    "LP4": "I retain information better when I engage in discussions and listen to experts.",
    "LP5": "I enjoy using technology, software, and simulations for learning.",
    "LP6": "I prefer learning through real-world case studies and industry applications."
}

# Collect answers via sliders
lp_answers = {}
for key, question in lp_questions.items():
    lp_answers[key] = st.slider(f"{key}: {question}", 1, 5, 3)

# Navigation buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back"):
        st.switch_page("pages/2_Personality Traits.py")

with col2:
    if st.button("Next →"):
        if 'answers' not in st.session_state:
            st.session_state['answers'] = {}
        st.session_state['answers'].update(lp_answers)
        st.switch_page("pages/4_Cognitive Strengths.py")
