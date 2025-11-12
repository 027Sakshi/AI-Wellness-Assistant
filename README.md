# AI-Powered Personalized Wellness Assistant

A smart health companion that links skin condition detection with personalized diet and exercise guidance.


## Prototype Showcase

> **Important Note:** This repository contains a **high-fidelity visual prototype**. The primary goal is to demonstrate the application's user interface (UI), user experience (UX), and complete feature flow.
>
> The back-end logic, machine learning models (CNNs), and database are **not** implemented in this version. All data (diagnoses, recommendations, and charts) is currently **mocked** for demonstration purposes.

---

## Problem & Solution

Current health apps are often siloed: skin-related apps focus only on detection, while fitness apps ignore underlying medical conditions.  
Our solution bridges this gap by providing a holistic, three-step wellness loop:

1. **Detect (Mocked):** The user uploads a skin image. The app (will) use a CNN model to diagnose the condition.  
2. **Recommend (Mocked):** Based on the diagnosis, the app generates personalized diet (eat/avoid), exercise, and lifestyle plans.  
3. **Track (Mocked):** The user tracks their progress, and the system's feedback loop (will) refine recommendations over time.

---

## Features (Showcased in Prototype)

- **Home Page:** Explains the project's mission, workflow, and team.  
- **Mock Diagnosis:** Upload image → select mock condition → view AI-style analysis card.  
- **Personalized Recommendations:** Custom diet, exercise, and lifestyle guidance per diagnosis.  
- **Progress Tracking:** Displays mock progress charts and feedback logging interface.  
- **Custom UI:** Beautiful interface styled with `assets/style.css`.

---

## Tech Stack (Prototype)

- **Core Framework:** Streamlit  
- **Data Handling:** Pandas (for mock charts)  
- **Animations:** Streamlit-Lottie  
- **Styling:** Custom HTML/CSS (injected via `assets/style.css`)  
- **Utilities:** Requests (for Lottie URLs)

---

## File Structure

```
AI-Wellness-Assistant/
├── app.py               # Main landing page (Home)
├── pages/               # Streamlit's multi-page directory
│   ├── 1_Diagnosis.py
│   ├── 2_Recommendations.py
│   └── 3_Progress_Tracking.py
├── assets/
│   └── style.css        # Custom styling
└── requirements.txt     # Python dependencies
```

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/AI-Wellness-Assistant.git
cd AI-Wellness-Assistant
```

### 2. Create a virtual environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```
The app should open automatically in your browser.

---

## Project Team

- **Presented by:** Sakshi Giglani, Bhavya Thakkar  
- **Guided by:** Dr. Madhuri Chopade


