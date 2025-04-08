# --- streamlit_app.py (Home Page) ---
import streamlit as st
from PIL import Image

st.set_page_config(page_title="LANDAS - Career Path Recommender", page_icon="💼", layout="centered")

import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Load the image
logo = Image.open("ALPHA.png")

# Convert to base64
buffered = BytesIO()
logo.save(buffered, format="PNG")
img_base64 = base64.b64encode(buffered.getvalue()).decode()

# Centered logo using HTML
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{img_base64}' width='150'/>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Centered Title and Tagline ---
st.markdown("""
<div style='text-align: center;'>
    <h1 style='margin-bottom: 0;'>L.A.N.D.A.S</h1>
    <h3 style='margin-bottom:0;'>Learners of ALPHA for Navigation Development and Alignment System</h3> 
    <h4 style='margin-top: 5px;'>A Career Path Recommender System from ALPHA</h4>
    <h5>Your Journey, Your Path, Your LANDAS 🚀</h5>
</div>
""", unsafe_allow_html=True)

# --- Description ---
st.markdown("""
This app will help match your personality, learning style, cognitive strengths, and professional capabilities with the job roles you're best suited for.

Click the button below to begin your journey.
""")

# --- Start Button ---
if st.button("🚀 Begin Assessment"):
    st.switch_page("pages/1_User_Info.py")

# --- Footer with Data Privacy Disclaimer ---
st.markdown("""
<hr style="margin-top: 50px; margin-bottom: 10px;"/>

<div style='font-size: 0.8em; color: gray; text-align: center;'>
    By clicking "Begin Assessment", you agree to the collection and use of your data in accordance with the <b>Philippine Data Privacy Act of 2012 (RA 10173)</b>. 
    All personal data will be used solely for career recommendation purposes and will not be shared with third parties.
</div>
""", unsafe_allow_html=True)
