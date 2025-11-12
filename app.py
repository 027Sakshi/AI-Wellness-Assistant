import streamlit as st
from streamlit_lottie import st_lottie
from streamlit.logger import get_logger
import requests

logger = get_logger(__name__)

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Wellness Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Function to load CSS ---
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Function to load Lottie animation ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load Assets ---
load_css("assets/style.css")
lottie_wellness = load_lottieurl("https://lottie.host/a392e25a-1c94-4328-a916-c50f14b6843c/iW3GYF3Fsh.json")

# --- Initialize Session State ---
# This holds the "diagnosis" that all pages can access.
if 'diagnosis' not in st.session_state:
    st.session_state.diagnosis = None
    st.session_state.confidence = 0
    st.session_state.summary = ""

# --- Sidebar Content ---
with st.sidebar:
    st.title("Project Info")
    st.markdown("""
        <div class="sidebar-info">
        <strong>Presented by:</strong>
        <ul>
            <li>Bhavya Thakkar</li>
            <li>Sakshi Giglani</li>
        </ul>
        <strong>Guided by:</strong>
        <ul>
            <li>Dr. Madhuri Chopade</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    st.info("This is a visual prototype for project showcase.")

# --- Main Page Content ---
st.markdown("<div class='home-title'>AI-Powered Personalized Wellness Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='home-tagline'>Your Smart Companion for Skin Health, Diet & Fitness</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.header(" ")
    st.subheader("Bridge the gap between healthcare and self-care")
    st.write(
        "This tool provides holistic support by not just identifying skin conditions, "
        "but also providing **actionable wellness plans** tailored to your needs."
    )
    
    # --- Main Navigation Buttons ---
    st.write(" ")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("Start Diagnosis ➡️", type="primary", use_container_width=True):
            st.switch_page("pages/1_🏥_Diagnosis.py")
    with c2:
        if st.button("See Recommendations 🥗", use_container_width=True):
            st.switch_page("pages/2_🥗_Recommendations.py")
    with c3:
        if st.button("Track Progress 📈", use_container_width=True):
            st.switch_page("pages/3_📈_Progress_Tracking.py")

    with st.expander("View Sample Workflow"):
        st.write("1. **Upload:** Go to the 'Diagnosis' page and upload an image of a skin condition.")
        st.write("2. **Analyze:** Our 'AI' will (currently mocked to) detect the condition.")
        st.write("3. **Recommend:** Based on the result, the 'Recommendations' page will show custom diet and exercise plans.")
        st.write("4. **Track:** Log your journey and see progress on the 'Progress Tracking' page.")

with col2:
    if lottie_wellness:
        st_lottie(lottie_wellness, height=350, key="wellness_lottie")