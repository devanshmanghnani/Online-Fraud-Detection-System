# Online_Fraud_Detection_System

This project uses a **Logistic Regression** machine learning model to detect fraudulent online financial transactions based on historical data. It covers data preprocessing, exploratory analysis, model training, evaluation, and web-based prediction using a Flask interface.

---

## 📚 Table of Contents

- [Project Overview](#project-overview)  
- [Data Collection](#data-collection)  
- [Data Preprocessing](#data-preprocessing)  
- [Exploratory Data Analysis](#exploratory-data-analysis)  
- [Feature Selection](#feature-selection)  
- [Model Training](#model-training)  
- [Evaluation and Testing](#evaluation-and-testing)  
- [Model Deployment](#model-deployment)  
- [Web Interface](#web-interface)  
- [Visualizations](#visualizations)

---

## 📌 Project Overview

The goal of this project is to identify whether a financial transaction is **fraudulent** or **genuine** using a Logistic Regression model. The key objectives include:

- Collecting and preparing transaction data  
- Analyzing and visualizing patterns of fraud  
- Building a Logistic Regression model for binary classification  
- Evaluating performance using accuracy and confusion matrix  
- Creating a user interface for prediction from user inputs

---

## 📥 Data Collection

The dataset used contains thousands of transaction records with fields such as:

- `type` (transaction type)  
- `amount` (transaction value)  
- `oldbalanceOrg`, `newbalanceOrig`  
- `oldbalanceDest`, `newbalanceDest`  
- `isFraud` (target label)

### 🛠 Libraries Used:
- `pandas`, `numpy`

---

## 🧹 Data Preprocessing

Key steps in data preparation:

- **Handling Missing Values**: Cleaned dataset by dropping or imputing missing entries  
- **Balancing the Dataset**: Applied **SMOTE** (Synthetic Minority Oversampling Technique) to handle class imbalance  
- **Encoding Categorical Data**: Converted categorical features using one-hot encoding  
- **Feature Scaling**: Applied `StandardScaler` for normalization

---

## 📊 Exploratory Data Analysis

- Analyzed fraud vs. non-fraud transaction patterns  
- Visualized high-risk transaction types  
- Charts: Bar charts, histograms, pie charts, and box plots

---

## 🎯 Feature Selection

- Selected relevant features using correlation and importance metrics  
- Removed irrelevant or non-informative columns  
- Evaluated model coefficients and visual feature importances

---

## 🧠 Model Training

- **Model Used**: Logistic Regression  
- **Split Ratio**: 80% training / 20% testing  
- Trained model using `scikit-learn`, saved with `joblib`  

---

## 🧪 Evaluation and Testing

- **Model Accuracy**: **94%**  
- Evaluated using:
  - Precision  
  - Recall  
  - F1-Score  
  - Confusion Matrix

- **Confusion Matrix**: Visual display of TP, TN, FP, FN

---

## 🚀 Model Deployment

- Used **Flask** for backend API development  
- Created endpoint to accept input and return prediction  
- Model loaded using `joblib` for fast predictions

---

## 🌐 Web Interface

- Simple HTML form to enter transaction details  
- Input data sent to Flask backend  
- Prediction result displayed instantly (Fraud / Not Fraud)

---

## 📊 Visualizations

- **Bar Chart**: Fraud vs. Non-Fraud transaction counts  
- **Pie Chart**: Percentage of fraud in dataset  
- **Histogram**: Transaction amount distribution  
- **Confusion Matrix Plot**: Model evaluation performance

---

