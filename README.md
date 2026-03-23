# 🚀 Telecom Churn Prediction System  
### Full Stack Machine Learning Project (FastAPI + ML Pipeline + Frontend)

---

## 📌 Project Overview

Customer churn is a major challenge in the telecom industry, directly impacting revenue and growth. This project leverages **Machine Learning and API-based architecture** to predict whether a customer is likely to churn based on key behavioral and billing features.

The system provides:

* Real-time churn prediction
* Backend API with validation and ML inference
* Interactive frontend for user input and results

---

## 🏗️ System Architecture

This project follows a **modular full-stack architecture**:

* **Frontend:** User interface for input and prediction display
* **Backend (FastAPI):** Handles API requests and ML inference
* **ML Pipeline:** Pre-trained model using Scikit-learn
* **Dataset & Notebook:** Used for training and experimentation

---

## 📂 Project Structure

```bash
TelecomChurnPrediction/
│
├── backend/
│   ├── main.py                  # FastAPI backend
│   └── model/
│       └── churn_pipeline.pkl   # ML pipeline model
│
├── frontend/                   # Frontend UI (multiple files)
│
├── churn_model.pkl             # Trained model (alternative)
├── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Dataset
├── Task_6_CustomerChurnTel.ipynb          # Training notebook
├── requirements.txt           # Python dependencies
├── package-lock.json          # Frontend dependencies
└── README.md
```

---

## ⚙️ Technologies Used

### 🔹 Backend

* FastAPI
* Uvicorn
* Pydantic (Data Validation)

### 🔹 Machine Learning

* Scikit-learn
* Pandas, NumPy
* Joblib (Model Serialization)

### 🔹 Frontend

* HTML, CSS, JavaScript
  *(or framework used)*

---

## 🔍 Backend API Details

The backend is built using **FastAPI** and provides a REST API for predictions.

### ✅ Endpoint: `/predict`

**Method:** POST

**Input:**

```json
{
  "tenure": 10,
  "MonthlyCharges": 70.5,
  "TotalCharges": 1500
}
```

### 🔒 Validation Rules

* Tenure: 0–100
* MonthlyCharges: 0–500
* TotalCharges: 0–10000

### 📤 Output:

```json
{
  "churn": "Yes"
}
```

The backend uses a **pre-trained ML pipeline** to process inputs and generate predictions. 

---

## 🤖 Machine Learning Pipeline

* Data preprocessing
* Feature engineering
* Model training using Scikit-learn
* Model saved using Joblib
* Integrated into backend for real-time inference

---

## 📊 Dataset

* Telecom customer dataset
* Includes:

  * Customer tenure
  * Billing information
  * Service usage patterns

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ishwarthecodddr/TelecomChurnPrediction.git
cd TelecomChurnPrediction
```

---

### 2️⃣ Run Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 3️⃣ Run Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🖥️ Frontend Preview

> 📸 Add your frontend screenshots below

### 🔹 Home Page

<!-- INSERT SCREENSHOT HERE -->

### 🔹 Input Form

<!-- INSERT SCREENSHOT HERE -->

### 🔹 Prediction Output

<!-- INSERT SCREENSHOT HERE -->

---

## 📈 Features

* Real-time churn prediction
* Clean API architecture
* Input validation with error handling
* ML pipeline integration
* Full-stack implementation

---

## 💡 Key Highlights

* End-to-end ML project (training → deployment)
* FastAPI-based scalable backend
* Industry-style project structure
* Ready for cloud deployment

---

## 🚀 Future Enhancements

* Deploy on AWS / Render / Azure
* Add authentication system
* Improve model with advanced algorithms (XGBoost, Deep Learning)
* Build analytics dashboard

---

## 👨‍💻 Team Members

* L ishwar
* Gaurav
* [Member 3 ]
* [Member 4 ]
* [Member 5 ]

---

## 📬 Conclusion

This project demonstrates the practical implementation of Machine Learning in solving real-world business problems using a scalable and production-ready architecture. It showcases strong skills in AI, backend development, and system design.

---

Thank you for your time and consideration.

Best regards,
**Team Telecom Churn Prediction**
B.Tech | KIIT University