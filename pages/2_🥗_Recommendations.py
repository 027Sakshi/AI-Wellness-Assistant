import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="🥗 Recommendations", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

load_css("assets/style.css")
lottie_fit = load_lottieurl("https://lottie.host/bb60b7a7-5a5f-4f36-b9d7-50ee2474b62c/yYH7HxtLzQ.json")

PLANS = {
    "Acne": {"eat": ["Leafy Greens", "Salmon", "Nuts & Seeds"], "avoid": ["Dairy", "Processed Foods"], "exercise": ["Yoga", "Cardio"]},
    "Eczema": {"eat": ["Avocado", "Probiotics", "Mackerel"], "avoid": ["Eggs", "Spices"], "exercise": ["Swimming", "Light Stretching"]},
    "Benign Nevi (Moles)": {"eat": ["Berries", "Carrots", "Oranges"], "avoid": ["None"], "exercise": ["General Fitness", "Sun Protection"]},
}

st.title("🥗 Personalized Recommendations")

if 'diagnosis' not in st.session_state:
    st.warning("Please complete a diagnosis first.")
else:
    d = st.session_state.diagnosis
    plan = PLANS[d]
    st.subheader(f"Wellness Plan for {d}")

    col1, col2 = st.columns([1.3, 1])
    with col1:
        tab1, tab2 = st.tabs(["🥦 Diet Plan", "🧘 Exercise Plan"])
        with tab1:
            st.markdown(f"<div class='recommend-card slide-in'><h4>Foods to Eat</h4><ul>{''.join(f'<li>{i}</li>' for i in plan['eat'])}</ul></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='recommend-card slide-in'><h4>Foods to Avoid</h4><ul>{''.join(f'<li>{i}</li>' for i in plan['avoid'])}</ul></div>", unsafe_allow_html=True)
        with tab2:
            st.markdown(f"<div class='recommend-card slide-in'><h4>Suggested Exercises</h4><ul>{''.join(f'<li>{i}</li>' for i in plan['exercise'])}</ul></div>", unsafe_allow_html=True)

        st.markdown("---")
        if st.button("📈 Go to Progress Tracking"):
            st.switch_page("pages/3_Progress_Tracking.py")

    with col2:
        if lottie_fit:
            st_lottie(lottie_fit, height=350, key="fitness_anim")

st.markdown("<hr><div class='footer'>🏠 <a href='../app.py'>Back to Home</a></div>", unsafe_allow_html=True)
