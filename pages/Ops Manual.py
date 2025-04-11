import streamlit as st

st.set_page_config(page_title="Operation Manual", page_icon="📘", layout="centered")

with st.sidebar:
    st.image("ALPHA.png", width=120)
    st.markdown("### Operation Manual")
    st.sidebar.progress(0.5 / 8)

st.title("📘 LANDAS Operation Manual")
st.markdown("Here's a quick visual guide on how to take the assessment:")

manual_images = [
    "assets/1_OpsManual.png",
    "assets/2_OpsManual.png",
    "assets/3_OpsManual.png",
    "assets/4_OpsManual.png"
]

for img_path in manual_images:
    st.image(img_path, use_column_width=True)
    st.markdown("---")

# Navigation buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("← Back to Homepage"):
        st.switch_page("LANDAS.py")

with col2:
    if st.button("✅ Got it! Proceed to Start"):
        st.switch_page("pages/2_User Info.py")
