import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open('churn_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_churn(features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    probability = model.predict_proba(df)[:, 1]
    return prediction[0], probability[0]

# Streamlit UI
st.set_page_config(page_title="Churn Prediction App", layout="wide")
st.title("📊 Expresso Churn Prediction App")
st.markdown("### Enter Customer Details to Predict Churn")

THEMES = {
    "Light": """
        <style>
        body { background-color: #f5f5f5; color: #000; }
        .stApp { background-color: #ffffff; }
        .css-18e3th9 { background-color: #ffffff; } /* Sidebar */
        .css-1d391kg { color: #000; }
        </style>
    """,
    "Dark": """
        <style>
        body { background-color: #1e1e1e; color: #ffffff; }
        .stApp { background-color: #121212; }
        .css-18e3th9 { background-color: #333; } /* Sidebar */
        .css-1d391kg { color: #fff; }
        </style>
    """,
    "Blue": """
        <style>
        body { background-color: #e3f2fd; color: #000; }
        .stApp { background-color: #bbdefb; }
        .css-18e3th9 { background-color: #64b5f6; } /* Sidebar */
        .css-1d391kg { color: #000; }
        </style>
    """,
}

# Sidebar for user inputs with better UI
with st.sidebar:
    st.image("expresso_logo.png", caption="Expresso Telecom")
    st.header("🔧 Settings")
    st.markdown("---")
    theme = st.sidebar.selectbox("Choose Theme", list(THEMES.keys()))
    st.markdown(THEMES[theme], unsafe_allow_html=True)
    st.sidebar.markdown("**Use the sidebar to change the theme!**")
    

# User Inputs
col1, col2 = st.columns(2)

region_mapping = {
    "DAKAR": 0, "DIOURBEL": 1, "FATICK": 2, "KAFFRINE": 3, "KAOLACK": 4,
    "KEDOUGOU": 5, "KOLDA": 6, "LOUGA": 7, "MATAM": 8, "SAINT-LOUIS": 9,
    "SEDHIOU": 10, "TAMBACOUNDA": 11, "THIES": 12, "ZIGUINCHOR": 13
}


with col1:
    region = st.selectbox("Region", list(region_mapping.keys()))
    encoded_region = region_mapping[region]
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=240, value=12)
    revenue = st.number_input("Revenue", min_value=0.0, value=500000.0)
    arpu_segment = st.number_input("ARPU Segment", min_value=0.0, value=60000.0)
    frequence = st.number_input("Call Frequency", min_value=0, value=200)
    data_volume = st.number_input("Data Volume Used (MB)", min_value=0.0, value=1500000.0)
    on_net = st.number_input("On-Net Calls", min_value=0, value=60000)

with col2:
    mrg = st.number_input("MRG", min_value=0, value=1)
    regularity = st.number_input("Regularity", min_value=0, value=100)
    freq_top_pack = st.number_input("Top Pack Frequency", min_value=0, value=3)
    avg_recharge_per_freq = st.number_input("Avg Recharge per Frequency", min_value=0.0, value=20000.0)
    revenue_per_recharge = st.number_input("Revenue per Recharge", min_value=0.0, value=15000.0)
    total_off_net_calls = st.number_input("Total Off-Net Calls", min_value=0, value=500)
    on_net_ratio = st.number_input("On-Net Ratio", min_value=0.0, value=0.9)
    data_per_usage = st.number_input("Data per Usage", min_value=0.0, value=2500.0)
    is_high_data_user = st.selectbox("High Data User", ["Yes", "No"])
    is_high_regular_user = st.selectbox("High Regular User", ["Yes", "No"])

# Prediction Button
if st.button("🚀 Predict Churn"):
    features = {
        "REGION": encoded_region,
        "TENURE": tenure,
        "REVENUE": revenue,
        "ARPU_SEGMENT": arpu_segment,
        "FREQUENCE": frequence,
        "DATA_VOLUME": data_volume,
        "ON_NET": on_net,
        "MRG": mrg,
        "REGULARITY": regularity,
        "FREQ_TOP_PACK": freq_top_pack,
        "avg_recharge_per_freq": avg_recharge_per_freq,
        "revenue_per_recharge": revenue_per_recharge,
        "total_off_net_calls": total_off_net_calls,
        "on_net_ratio": on_net_ratio,
        "data_per_usage": data_per_usage,
        "is_high_data_user": 1 if is_high_data_user == "Yes" else 0,
        "is_high_regular_user": 1 if is_high_regular_user == "Yes" else 0
    }
    prediction, probability = predict_churn(features)
    
    if prediction == 1:
        st.error(f"⚠️ This customer is likely to churn with a probability of {probability:.3f}")
    else:
        st.success(f"✅ This customer is not likely to churn. Probability: {probability:.3f}")

# Footer with additional information
st.markdown("---")
st.markdown("Developed by Osato Osazuwa | Contact: osato.osazuwa@gmail.com")
