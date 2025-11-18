import streamlit as st
from utils.FactorsData import FactorsData
from utils.config import (
    APP_NAME, 
    VERSION, 
    encoder_preprocessor, 
    scaler_preprocessor, 
    logistic_regression_model, 
    random_forest_model
)
from utils.inference import predict_new

# Page configuration
st.set_page_config(
    page_title=APP_NAME,
    page_icon="🌱",
    layout="centered"
)

# Title and version
st.title(f"🌱 {APP_NAME}")
st.caption(f"Version {VERSION}")

# Main content
st.header("Soil & Environmental Factors")
st.write("Enter the soil and environmental parameters for crop prediction:")

# Model selection with custom styling
st.markdown("### 🤖 Choose Prediction Model")

# Initialize session state if not exists
if 'model_choice' not in st.session_state:
    st.session_state.model_choice = "Random Forest"

col_rf, col_lr = st.columns(2)

with col_rf:
    button_type = "primary" if st.session_state.model_choice == "Random Forest" else "secondary"
    if st.button("🌲 Random Forest", use_container_width=True, type=button_type, key="btn_rf"):
        st.session_state.model_choice = "Random Forest"
        st.rerun()

with col_lr:
    button_type = "primary" if st.session_state.model_choice == "Logistic Regression" else "secondary"
    if st.button("📈 Logistic Regression", use_container_width=True, type=button_type, key="btn_lr"):
        st.session_state.model_choice = "Logistic Regression"
        st.rerun()

st.divider()

# Create input form
with st.form("prediction_form"):
    st.subheader("Input Features")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        N = st.number_input(
            "Nitrogen (N)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            help="Nitrogen content in soil"
        )
        P = st.number_input(
            "Phosphorus (P)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            help="Phosphorus content in soil"
        )
        K = st.number_input(
            "Potassium (K)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            help="Potassium content in soil"
        )
        temperature = st.number_input(
            "Temperature (°C)",
            min_value=8.0,
            max_value=50.0,
            value=25.0,
            step=0.1,
            help="Temperature of the environment (8-50°C)"
        )
    
    with col2:
        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=0.1,
            help="Atmospheric moisture level (0-100%)"
        )
        ph = st.number_input(
            "pH Level",
            min_value=0.0,
            max_value=14.0,
            value=7.0,
            step=0.1,
            help="Soil acidity/alkalinity"
        )
        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            help="Annual or seasonal rainfall"
        )
    
    # Submit button
    submitted = st.form_submit_button("🔮 Get Prediction", type="primary", use_container_width=True)
    
    if submitted:
        try:
            # Create FactorsData instance
            data = FactorsData(
                N=N,
                P=P,
                K=K,
                temperature=temperature,
                humidity=humidity,
                ph=ph,
                rainfall=rainfall
            )
            
            # Select model based on user choice
            if st.session_state.model_choice == "Random Forest":
                model = random_forest_model
                model_name = "Random Forest"
            else:
                model = logistic_regression_model
                model_name = "Logistic Regression"
            
            # Show loading spinner
            with st.spinner(f'Running prediction with {model_name}...'):
                result = predict_new(
                    data=data,
                    preprocessor=scaler_preprocessor,
                    label_encoder=encoder_preprocessor,
                    model=model
                )
            
            # Display results
            st.success("✅ Prediction completed!")
            
            st.subheader("📊 Results")
            st.json(result)
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.exception(e)

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: gray; padding: 20px;'>
        <p>🌱 Crop Prediction System </p>
        <p>Made by Eng. Ahmed Shoaib</p>
    </div>

""", unsafe_allow_html=True)
