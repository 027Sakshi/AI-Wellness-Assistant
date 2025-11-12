import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="📈 Progress Tracking", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

load_css("assets/style.css")
lottie_progress = load_lottieurl("https://lottie.host/9f35120a-328b-49f0-9851-12b8c74c7a15/2m2tCwKPVv.json")

st.title("📈 Progress Tracking")
st.write("Track your wellness journey and visualize improvements over time.")

col1, col2 = st.columns([1.4, 1])
with col1:
    data = pd.DataFrame({"Week": range(1, 8), "Severity": [8, 8, 7, 6, 5, 4, 3], "Adherence": [4, 6, 7, 8, 7, 8, 9]}).set_index("Week")
    st.line_chart(data)

    st.subheader("📝 Submit Feedback")
    severity = st.slider("Symptom Severity (10 = worst)", 0, 10, 5)
    adherence = st.slider("Plan Adherence (10 = perfect)", 0, 10, 7)
    note = st.text_area("Additional Notes (optional)")

    if st.button("Log Progress", type="primary"):
        st.success("Your feedback has been logged successfully! 🎉")

with col2:
    if lottie_progress:
        st_lottie(lottie_progress, height=350, key="progress_lottie")

st.markdown("<hr><div class='footer'>🏠 <a href='../app.py'>Back to Home</a></div>", unsafe_allow_html=True)
