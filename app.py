import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Wellness Assistant",
    page_icon="🤖",
    layout="wide",
)

# ---------- HELPER FUNCTIONS ----------
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------- LOAD ASSETS ----------
load_css("assets/style.css")
lottie_home = load_lottieurl("https://lottie.host/1f30d548-d3f3-4a6b-bd3f-0ed8a19564ed/t7CzPEnY0s.json")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image("https://img.icons8.com/?size=80&id=12253&format=png", width=60)
    st.markdown("## Project Overview")
    st.info("""
    AI-Powered Personalized Wellness Assistant  
    *Detects skin conditions and provides personalized diet and exercise guidance.*
    """)
    st.markdown("**Presented by:** Sakshi Giglani & Bhavya Thakkar  \n**Guided by:** Dr. Madhuri Chopade")

# ---------- MAIN HEADER ----------
st.markdown("<div class='home-title slide-in'>AI-Powered Personalized Wellness Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='home-tagline fade-in'>Your Smart Companion for Skin Health, Diet & Fitness</div>", unsafe_allow_html=True)

# ---------- CONTENT LAYOUT ----------
col1, col2 = st.columns([1.3, 1])

with col1:
    st.subheader("💡 Why This Project?")
    st.write("""
    Many people ignore early signs of skin issues and follow generic advice.
    Our assistant bridges this gap by combining **AI-based skin diagnosis** 
    and **personalized lifestyle guidance** into one seamless system.
    """)

    st.markdown("### 🌐 Key Features")
    st.markdown("""
    - 🩺 Detects skin diseases from uploaded images  
    - 🥗 Generates condition-specific diet and fitness plans  
    - 📈 Tracks recovery and adapts recommendations  
    - 🤖 Integrates AI for adaptive feedback
    """)

    # --- Navigation Buttons ---
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🏥 Start Diagnosis", use_container_width=True, type="primary"):
            st.switch_page("pages/1_Diagnosis.py")
    with c2:
        if st.button("🥗 Recommendations", use_container_width=True):
            st.switch_page("pages/2_Recommendations.py")
    with c3:
        if st.button("📈 Track Progress", use_container_width=True):
            st.switch_page("pages/3_Progress_Tracking.py")

    with st.expander("🎬 View Workflow"):
        st.markdown("""
        **Step 1:** Upload skin image → AI detects condition  
        **Step 2:** Personalized diet & exercise plan generated  
        **Step 3:** Track health improvements and feedback  
        **Step 4:** Refined guidance based on your progress  
        """)

with col2:
    if lottie_home:
        st_lottie(lottie_home, height=400, key="wellness_home")

# ---------- FOOTER ----------
st.markdown("""
<hr style="margin-top:2rem;">
<div class="footer">
🤖 <b>AI-Powered Wellness Assistant</b> | Designed by <b>Sakshi Giglani</b> & <b>Bhavya Thakkar</b> | Guided by <b>Dr. Madhuri Chopade</b>
</div>
""", unsafe_allow_html=True)
