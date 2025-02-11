# Expresso Churn Prediction Project

## 📌 Project Overview
Expresso is an African telecommunications company operating in **Mauritania and Senegal**. This project aims to **predict customer churn** using historical customer data. The goal is to identify at-risk customers and provide actionable insights to **reduce churn rates**.

## 📊 Dataset
The dataset contains **2.5 million records** with customer behavioral data. The key features include:
- **Categorical:** `REGION`, `TOP_PACK`
- **Numerical:** `TENURE`, `MONTANT`, `FREQUENCE_RECH`, `REVENUE`, `ARPU_SEGMENT`, `FREQUENCE`, `DATA_VOLUME`, `ON_NET`, `ORANGE`, `TIGO`, `ZONE1`, `ZONE2`, `MRG`, `REGULARITY`, `FREQ_TOP_PACK`
- **Target Variable:** `CHURN` (1 = churn, 0 = not churn)

## ⚙️ Steps Implemented
### 🔍 Data Preprocessing & Feature Engineering
- **Handled Missing & Corrupt Data**
- **Removed Duplicates & Outliers**
- **Engineered New Features:**
  - `is_new_customer`: Identifies customers with tenure < 6 months.
  - `avg_recharge_per_freq`: Average recharge per frequency.
  - `revenue_per_recharge`: Revenue per recharge.
- **Encoded Categorical Variables** using label encoding.

### 🏋️ Model Training
- Trained multiple **ML models**:
  - Logistic Regression- `94.15%`
  - Gradient Boosting - `94.28%`
  - Random Forest- `93.7%`
  - XGBoost- `94.3%`
- **Evaluated Performance** using classification report and confusion matrix.

### 🖥️ Streamlit App
A **user-friendly Streamlit web app** was developed for real-time churn predictions:
- **Input Fields** for feature values
- **Predict Button** to classify users as churners or non-churners


## 🚀 How to Run the Project
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Run the Streamlit App
Here's the app link - [streamlit app link](https://churn-prediction123.streamlit.app/)

## 📌 Future Improvements
- Implement **Deep Learning models** for better accuracy.
- Enhance **feature selection** for optimized predictions.
- Add **automated reports** with insights for business teams.

📩 **Contact:** osato.osazuwa@gmail.com

