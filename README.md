# SONAR-Rock-and-Mine-Prediction


# SONAR Rock vs Mine Prediction

This project is a binary classification task that uses machine learning to predict whether an object is a rock or a mine based on SONAR signal data. The dataset used contains 60 features representing the energy of sonar signals reflected by the object.

## 📊 Problem Statement

Given SONAR returns bounced off a surface under the sea, determine whether the object is a **Rock** or a **Mine**. This is important for undersea navigation and detection systems (like in submarines or marine exploration).

## 🧠 Machine Learning Approach

- Problem Type: Binary Classification
- Algorithms Tried:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Random Forest
  - K-Nearest Neighbors (KNN)
  - XGBoost (optional)

## 📁 Dataset

- **Source**: [UCI Machine Learning Repository - SONAR Dataset](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks))
- **Features**: 60 numerical attributes (sonar frequencies)
- **Target**: Label ("R" for rock, "M" for mine)

## ✅ Project Workflow

1. **Data Loading**  
2. **Exploratory Data Analysis (EDA)**  
3. **Data Preprocessing**
   - Label Encoding (`R` → 0, `M` → 1)
   - Train-Test Split
   - Feature Scaling
4. **Model Training & Evaluation**
   - Accuracy, Confusion Matrix, Classification Report
5. **Model Deployment** (optional)
   - Streamlit or Flask App

## 🧪 Results

| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression| ~85%     |
| SVM                | ~88%     |
| Random Forest      | ~89%     |
| KNN                | ~86%     |
| XGBoost (opt)      | ~90%+    |

> Actual results may vary depending on tuning and cross-validation.

## 📦 Dependencies

Install required packages using:

```bash
pip install -r requirements.txt
