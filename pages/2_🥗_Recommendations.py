import streamlit as st

# Function to load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("assets/style.css")

# --- Mock Data for Plans ---
PLANS = {
    "Acne": {
        "eat": ["🥦 Leafy Greens", "🍣 Salmon (Omega-3s)", "🥜 Zinc (Nuts, Seeds)"],
        "avoid": ["🥛 Dairy Products", "🍩 High-Glycemic Foods", "🍔 Greasy/Processed Foods"],
        "exercise": ["🧘 Yoga (Stress Reduction)", " cardio (Blood Circulation)"]
    },
    "Eczema": {
        "eat": ["🥑 Avocado (Healthy Fats)", " probiotics (Yogurt, Kefir)", "🐟 Mackerel (Anti-inflammatory)"],
        "avoid": ["🥚 Eggs (Common Allergen)", "🌶️ Spicy Foods", "🍅 Nightshades (for some)"],
        "exercise": ["🏊 Swimming (Cooling)", " low-impact cardio"]
    },
    "Benign Nevi (Moles)": {
        "eat": ["🍓 Berries (Antioxidants)", "🥕 Carrots (Vitamin A)", "🍊 Oranges (Vitamin C)"],
        "avoid": ["- General skin health, no specific avoidances."],
        "exercise": ["- General fitness", "☀️ **Priority:** Sun Protection (UPF Clothing, Shade)"]
    },
    "default": {
        "eat": ["- Please get a diagnosis first."],
        "avoid": ["-"],
        "exercise": ["-"]
    }
}

st.title("🥗 Personalized Recommendations")

# --- Check if Diagnosis Exists ---
if 'diagnosis' not in st.session_state or st.session_state.diagnosis is None:
    st.warning("Please upload an image on the 'Diagnosis' page first.")
    if st.button("Go to Diagnosis ⬅️"):
        st.switch_page("pages/1_🏥_Diagnosis.py")
else:
    diagnosis = st.session_state.diagnosis
    plan = PLANS.get(diagnosis, PLANS["default"])
    
    st.header(f"Your Personalized Plan for: **{diagnosis}**")
    st.write("Based on your condition, here are lifestyle suggestions to support your wellness.")
    
    tab1, tab2 = st.tabs(["🥦 Diet Plan", "🧘 Exercise Plan"])
    
    with tab1:
        st.markdown(
            f"""
            <div class="recommend-card-eat">
                <div class="card-header">🥦 Foods to Eat</div>
                <ul>{''.join(f'<li>{item}</li>' for item in plan['eat'])}</ul>
            </div>
            <div class="recommend-card-avoid">
                <div class="card-header">🚫 Foods to Avoid</div>
                <ul>{''.join(f'<li>{item}</li>' for item in plan['avoid'])}</ul>
            </div>
            """, unsafe_allow_html=True
        )

    with tab2:
        st.markdown(
            f"""
            <div class="recommend-card-exercise">
                <div class="card-header">🧘 Suggested Exercises</div>
                <ul>{''.join(f'<li>{item}</li>' for item in plan['exercise'])}</ul>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("---")
    st.subheader("🤖 Get Daily Tips")
    if st.button("Get a Daily Wellness Tip (Mock LLM)"):
        # This mocks the LLM call
        tips = [
            "Tip: Remember to drink at least 8 glasses of water today to support skin hydration!",
            "Tip: A 10-minute walk after meals can aid digestion and improve overall health.",
            "Tip: Try a 5-minute mindfulness session to reduce stress, which can be a trigger for skin inflammation."
        ]
        st.info(f"**Tip of the Day:** {tips[hash(diagnosis) % len(tips)]}")