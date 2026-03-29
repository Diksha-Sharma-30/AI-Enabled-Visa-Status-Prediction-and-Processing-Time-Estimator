# AI-Enabled Visa Status Prediction and Processing Time Estimator

## 📌 Overview
This project applies **machine learning** to predict visa application outcomes and estimate processing times. It is designed to assist applicants, consultants, and policymakers by providing data-driven insights into visa decisions.

## WebAPP LINK- https://visa-status-prediction-time-estimator-diksha.streamlit.app/ 
---

## 🚀 Features
- Visa status prediction (*Approved*, *Rejected*, *Pending*)
- Processing time estimation based on historical data
- Data preprocessing and feature engineering
- Predictive modeling pipeline (classification + regression)
- Visualization and reporting

---

## 🛠️ Tech Stack
- **Languages**: Python, SQL
- **Frameworks**: Flask/Django, React
- **Libraries**: scikit-learn, pandas, numpy, matplotlib, seaborn
- **Tools**: Jupyter Notebook, GitHub Actions (CI/CD)

---

## 📂 Project Structure
  
AI-Visa-Prediction/
│── data/                # Raw and processed datasets
│── notebooks/           # EDA and experiments
│── src/                 # Source code (models, preprocessing, API)
│── docs/                # Documentation and reports
│── tests/               # Unit and integration tests
│── requirements.txt     # Dependencies
│── README.md            # Project overview


---

## ⚙️ Workflow
1. **Data Collection** → Import historical visa datasets  
2. **Preprocessing** → Clean, encode, normalize features  
3. **EDA** → Identify trends and correlations  
4. **Model Training** → Classification & regression models  
5. **Evaluation** → Accuracy, F1-score, RMSE  
6. **Deployment** → REST API / Web interface  

---

## 📊 Example Use Case
**Input:** Applicant details (country, occupation, education, prior visa history)  
**Output:**  
- Predicted status: *Approved*  
- Estimated processing time: *3.5 months*  

---

## ✅ Installation
```bash
git clone https://github.com/Diksha-Sharma-30/AI-Enabled-Visa-Status-Prediction-and-Processing-Time-Estimator.git
cd AI-Enabled-Visa-Status-Prediction-and-Processing-Time-Estimator
pip install -r requirements.txt

Run locally:
python src/app.py
API endpoint:
http://localhost:5000/predict

📌 Future Enhancements
Real-time immigration dataset integration

Deep learning models for improved accuracy

Interactive dashboard for applicants/consultants

Multi-country visa category support
