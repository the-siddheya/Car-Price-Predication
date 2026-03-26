# 🚗 Smart Car Price Predictor

An end-to-end Machine Learning project that predicts the resale value of used cars based on key features like company, model, year, fuel type, and kilometers driven. The project is deployed using a modern Streamlit web application.

---

## 🚀 Project Overview

This project aims to estimate car resale prices using machine learning techniques. It covers the full pipeline from data analysis and preprocessing to model building and deployment through an interactive UI.

---

## ✨ Features

- 🚗 Predicts resale value of used cars  
- 📊 Exploratory Data Analysis (EDA)  
- 🧹 Data preprocessing & feature engineering  
- 🤖 Machine Learning regression model  
- 🌐 Interactive web app using Streamlit  
- 💰 Displays predicted price with range  
- 🎨 Premium UI (Dark futuristic design)  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Streamlit  
- Pickle  

---

## 🔄 Workflow

- Data Collection  
- Data Cleaning  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Model Training & Evaluation  
- Model Saving (Pickle)  
- Deployment using Streamlit  

---

## 📂 Project Structure


├── app.py
├── CPP.pkl
├── clean_data.csv
├── 01_eda_raw_data.ipynb
├── 02_data_preprocessing.ipynb
├── 03_model_inference.ipynb
├── README.md


---

## ▶️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Dependencies
pip install -r requirements.txt
3. Run the App
streamlit run app.py
💡 Example
Input:
Company: Maruti
Model: Swift
Year: 2018
Fuel Type: Petrol
KM Driven: 40,000
Output:

💰 Estimated Price: ₹4,50,000
📊 Range: ₹4,14,000 — ₹4,86,000

🎯 Future Improvements
Add real-time model confidence score
Improve accuracy using advanced models (XGBoost, Random Forest)
Add more features (location, ownership, transmission)
Deploy on cloud (Streamlit Cloud / AWS)
Enhance UI/UX further
🧠 Key Learnings
End-to-end Machine Learning pipeline
Data preprocessing & feature engineering
Regression model building
Model deployment using Streamlit
Building real-world ML applications
👨‍💻 Author

Siddheya Pitambare
