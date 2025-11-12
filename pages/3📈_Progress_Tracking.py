import streamlit as st
import pandas as pd
import numpy as np

# Function to load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("assets/style.css")

st.title("📈 Progress Tracking")
st.write("Track your progress over time using feedback and observation.")

# --- Mock Progress Chart ---
st.header("Mock Progress Chart")
st.write("This chart demonstrates how your self-reported feedback could be tracked.")

# Create fake data
chart_data = pd.DataFrame(
    {
        "Week": [1, 2, 3, 4, 5, 6, 7],
        "Symptom Severity (Reported)": [8, 8, 7, 6, 5, 4, 3],
        "Plan Adherence (Reported)": [4, 6, 7, 8, 7, 8, 9]
    }
).set_index("Week")

st.line_chart(chart_data)

st.markdown("---")


# --- Feedback Input ---
st.header("Submit Your Weekly Feedback")
st.write("Your feedback helps the system refine its recommendations over time.")

symptom_level = st.slider("How would you rate your symptom severity this week? (10 = Worst)", 0, 10, 5)
adherence_level = st.slider("How well did you adhere to the wellness plan? (10 = Perfectly)", 0, 10, 7)
feedback_text = st.text_area("Any additional notes for this week? (e.g., 'I felt great after yoga!')")

if st.button("Log My Progress", type="primary"):
    # In a real app, this would save to a database
    st.toast("Your progress has been logged! The system will learn from this.", icon="🎉")
    
    # You could add to a session_state list here to show a history