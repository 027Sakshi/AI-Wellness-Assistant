import streamlit as st
import time

# Function to load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("assets/style.css")

# --- Mock Data for Showcase ---
MOCK_DATA = {
    "Acne": {
        "confidence": 0.92,
        "summary": "Acne is a common skin condition that happens when hair follicles under the skin become clogged. This mock-up will generate a plan focused on anti-inflammatory foods."
    },
    "Eczema": {
        "confidence": 0.88,
        "summary": "Eczema (Atopic Dermatitis) causes patches of skin to become inflamed, itchy, and rough. This mock-up will generate a plan focused on hydration and identifying trigger foods."
    },
    "Benign Nevi (Moles)": {
        "confidence": 0.95,
        "summary": "These are common, non-cancerous skin growths. While not a 'disease' to be treated with diet, we'll provide general skin health and protection advice."
    }
}

st.title("🏥 Skin Diagnosis")
st.write("Upload an image of the skin condition for analysis.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Image for Analysis", width=300)
    
    # Dropdown to select the *type* of mock output for the demo
    mock_condition = st.selectbox(
        "Select a mock diagnosis for this demo:",
        ("Acne", "Eczema", "Benign Nevi (Moles)")
    )
    
    if st.button("Analyze Image", type="primary"):
        with st.spinner("AI is analyzing the image..."):
            time.sleep(2) # Simulate analysis time
        
        # --- Save to Session State ---
        data = MOCK_DATA[mock_condition]
        st.session_state.diagnosis = mock_condition
        st.session_state.confidence = data["confidence"]
        st.session_state.summary = data["summary"]
        
        st.success("Analysis Complete!")

# --- Display Results (if diagnosis exists in state) ---
if st.session_state.diagnosis:
    st.markdown("---")
    st.header("Analysis Result")
    
    confidence_level = st.session_state.confidence
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Detected Condition", st.session_state.diagnosis)
        st.metric("Confidence", f"{confidence_level*100:.0f}%")
        st.progress(int(confidence_level * 100))
        
    with col2:
        st.markdown(f"""
        <div class="summary-card">
            <div class="card-title">Condition Summary</div>
            <p>{st.session_state.summary}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("Your personalized wellness plan is ready. Proceed to the next step.")
    if st.button("See My Recommendations ➡️", use_container_width=True):
        st.switch_page("pages/2_🥗_Recommendations.py")