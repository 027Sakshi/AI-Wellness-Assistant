import streamlit as st
from streamlit_lottie import st_lottie
import time, requests

st.set_page_config(page_title="🏥 Diagnosis", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

load_css("assets/style.css")
lottie_ai = load_lottieurl("https://lottie.host/79c8ad39-1280-45ac-8973-022ba60d4a9d/fPcehEHDyG.json")

st.title("🏥 Skin Diagnosis")
st.write("Upload an image to simulate AI-based skin condition detection.")

MOCK_DATA = {
    "Acne": {"confidence": 0.92, "summary": "Acne occurs when follicles clog with oil and dead skin. Focus on hydration and anti-inflammatory foods."},
    "Eczema": {"confidence": 0.88, "summary": "Eczema leads to itchy, inflamed patches. Prioritize moisturizing and avoiding triggers."},
    "Benign Nevi (Moles)": {"confidence": 0.95, "summary": "These are harmless moles. Maintain skin health through good nutrition and sun protection."}
}

col1, col2 = st.columns([1.3, 1])
with col1:
    uploaded_file = st.file_uploader("Upload skin image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", width=300)
        mock_condition = st.selectbox("Select Mock Diagnosis:", list(MOCK_DATA.keys()))

        if st.button("🔍 Analyze Image", type="primary"):
            with st.spinner("AI analyzing image..."):
                time.sleep(2)
            data = MOCK_DATA[mock_condition]
            st.session_state.diagnosis = mock_condition
            st.session_state.confidence = data["confidence"]
            st.session_state.summary = data["summary"]
            st.success("Analysis Complete ✅")

    if 'diagnosis' in st.session_state:
        st.markdown("---")
        colA, colB = st.columns([1, 2])
        with colA:
            st.metric("Detected Condition", st.session_state.diagnosis)
            st.metric("Confidence", f"{st.session_state.confidence*100:.0f}%")
            st.progress(int(st.session_state.confidence * 100))
        with colB:
            st.markdown(f"<div class='summary-card slide-in'><h4>Condition Summary</h4><p>{st.session_state.summary}</p></div>", unsafe_allow_html=True)

        st.info("Your personalized plan is ready. Proceed to recommendations ➡️")
        if st.button("🥗 See My Recommendations"):
            st.switch_page("pages/2_Recommendations.py")
    else:
        if lottie_ai:
            st_lottie(lottie_ai, height=400, key="ai_scan")

st.markdown("<hr><div class='footer'>🏠 <a href='../app.py'>Back to Home</a></div>", unsafe_allow_html=True)
