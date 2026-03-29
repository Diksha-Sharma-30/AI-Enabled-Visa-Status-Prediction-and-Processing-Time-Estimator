import streamlit as st
from predict import predict_processing_time
import time
import base64

# -------------------------------
# Background Image Function
# -------------------------------
def add_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(f"""
<style>

/* Background */
.stApp {{
    background-image: url("data:image/png;base64,{encoded}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* LEFT SHIFT CONTAINER */
.main-container {{
    width: 600px;
    margin-left: 8%;
    margin-top: 50px;
}}

/* Glass Card - LIGHT (GitHub style) */
.glass {{
    background: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
}}

/* TEXT COLORS (NAVY BLUE) */
h1, h2, h3, label, p {{
    color: #0f172a !important;
    font-weight: 600;
}}

/* Inputs */
.stSelectbox, .stNumberInput, .stDateInput {{
    border-radius: 10px;
}}

/* Input labels */
.css-1cpxqw2 {{
    color: #0f172a !important;
}}

/* Button */
.stButton>button {{
    background: linear-gradient(90deg, #1e3a8a, #2563eb);
    color: white;
    font-size: 17px;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    border: none;
    font-weight: 600;
}}

/* Success / info text */
.stAlert {{
    border-radius: 10px;
}}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Visa Predictor", page_icon="🛂")

# 🔹 Add your background image here
add_bg("vs16.avif")   # <-- keep image in same folder

# -------------------------------
# UI Container
# -------------------------------
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.title("🛂 Visa Processing Time Predictor")
st.markdown("### ✨ Smart AI Estimation System")

# -------------------------------
# Dropdown options
# -------------------------------
visa_classes = ['E-3 Australian', 'H-1B', 'H-1B1 Chile', 'H-1B1 Singapore']

states = ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','GU','HI','IA','ID',
          'IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MP','MS','MT','NC',
          'ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','PR','RI','SC','SD',
          'TN','TX','UT','VA','VI','VT','WA','WI','WV','WY']

# -------------------------------
# Inputs
# -------------------------------
visa_class = st.selectbox("Visa Class", visa_classes)
full_time = st.radio("Full Time Position", ["Y", "N"])

col1, col2 = st.columns(2)
with col1:
    employer_state = st.selectbox("Employer State", states)
with col2:
    worksite_state = st.selectbox("Worksite State", states)

wage = st.number_input("💰 Wage ($)", min_value=0.0, step=1000.0)
prev_wage = st.number_input("💰 Prevailing Wage ($)", min_value=0.0, step=1000.0)

application_date = st.date_input("📅 Application Date")

# -------------------------------
# Prediction
# -------------------------------
if st.button("🚀 Predict Now"):

    if wage <= 0 or prev_wage <= 0:
        st.error("❌ Salary must be greater than 0")

    else:
        input_data = {
            "VISA_CLASS": visa_class,
            "FULL_TIME_POSITION": full_time,
            "EMPLOYER_STATE": employer_state,
            "WORKSITE_STATE": worksite_state,
            "WAGE_RATE_OF_PAY_FROM": wage,
            "PREVAILING_WAGE": prev_wage,
            "application_date": str(application_date)
        }

        with st.spinner("🤖 AI is predicting..."):
            time.sleep(1)
            result = predict_processing_time(input_data)

        st.success(f"🎯 Estimated Processing Time: **{result} days**")

        # Interpretation
        if result < 10:
            st.info("⚡ Very fast processing")
        elif result < 50:
            st.info("👍 Normal processing time")
        else:
            st.warning("⏳ May take longer")

        # Range
        st.markdown(f"📊 Range: **{max(0, result-5)} - {result+5} days**")

        # Progress bar
        st.progress(min(int(result), 100))

        # Chart
        st.bar_chart({"Processing Days": [result]})

st.markdown('</div>', unsafe_allow_html=True)