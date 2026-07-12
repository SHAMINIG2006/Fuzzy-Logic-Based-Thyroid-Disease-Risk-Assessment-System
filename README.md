# 🩺 Fuzzy Logic–Based Thyroid Disease Risk Assessment System (ECHRS)

## 📌 Overview

The **Environmental-Clinical Hybrid Risk Scoring (ECHRS)** system is an AI-powered healthcare application designed to estimate thyroid disease risk by combining **clinical thyroid parameters** with **environmental exposure factors**.

Unlike traditional prediction systems that rely only on laboratory results, this project integrates environmental indicators such as pollution and nitrate exposure to generate a personalized, percentage-based thyroid risk score for early diagnosis.

---

## 🎯 Problem Statement

Most thyroid disease prediction systems consider only biochemical parameters such as thyroid hormone levels. They often:

* Ignore environmental risk factors
* Produce only binary predictions (Normal/Abnormal)
* Cannot identify borderline-risk patients
* Lack personalized risk assessment
* Provide limited interpretability

This project addresses these limitations using a hybrid risk-scoring framework.

---

## 💡 Proposed Solution

The proposed **Environmental-Clinical Hybrid Risk Scoring (ECHRS)** framework combines:

* Clinical prediction using Deep Learning
* Environmental risk scoring
* Percentage-based hybrid risk calculation
* Risk classification into Low, Moderate, and High categories

The final prediction provides a more comprehensive assessment than conventional thyroid diagnosis methods.

---

## ✨ Key Features

* Hybrid Clinical + Environmental Risk Assessment
* Deep Learning-Based Prediction
* Percentage-Based Risk Score
* Personalized Health Assessment
* Early Warning System
* Interactive Web Dashboard
* Explainable Risk Categories

---

## 🏗️ System Workflow

```text
Clinical Data
(T3, TT4, T4U, FTI)
        │
        ▼
Data Preprocessing
        │
        ▼
Dropout ANN Model
        │
        ▼
Clinical Risk Score
        │
        ├───────────────┐
        │               │
Environmental Data      │
(Pollution, Nitrate)    │
        │               │
        ▼               │
Environmental Risk      │
        │               │
        └──────┬────────┘
               ▼
Hybrid Risk Scoring (ECHRS)
               ▼
Risk Percentage
               ▼
Low / Moderate / High
```

---

## 🤖 Machine Learning Models

| Model | Accuracy |
|--------|----------|
| Artificial Neural Network (ANN) | 82.27% |
| Deep Neural Network (DNN) | 82.44% |
| **Dropout ANN (Final Model)** | **82.88% Test Accuracy** |

The Dropout ANN achieved the best balance between accuracy and generalization and was selected as the final prediction model.

---

## 📊 Dataset

**Source:** UCI Machine Learning Repository

### Dataset Information

* 9,172 Patient Records
* 31 Clinical Features

### Selected Clinical Features

* TSH
* T3
* TT4
* T4U
* FTI

### Environmental Features

* Pollution Index
* Nitrate Level

---

## ⚙️ Technologies Used

* Python
* TensorFlow
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Google Colab
* Flask
* HTML
* CSS

---

## 📈 Results

The proposed ECHRS model successfully:

* Combined clinical and environmental information
* Generated personalized thyroid risk scores
* Classified patients into Low, Moderate, and High Risk
* Improved interpretability using percentage-based scoring
* Achieved **82.88% test accuracy** using Dropout ANN

---

## 💻 Web Dashboard

The project includes a web dashboard that allows users to:

* Enter clinical measurements
* Provide environmental information
* View hybrid thyroid risk score
* Receive Low, Moderate, or High risk prediction
* Understand their personalized health assessment

---

## 🚀 Future Improvements

* Real-time environmental data integration
* IoT sensor support
* Explainable AI (SHAP/LIME)
* Transformer-based deep learning models
* Mobile application
* Cloud deployment
* Multi-country clinical datasets

---

## 📂 Project Structure

```
ECHRS/
│
├── dataset/
├── notebooks/
├── models/
├── static/
├── templates/
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 🎯 Project Highlights

* AI for Healthcare
* Deep Learning
* Hybrid Risk Scoring
* Environmental + Clinical Analysis
* Personalized Risk Prediction
* Healthcare Analytics
* Web-Based Dashboard

---

## 👩‍💻 Developed By

**Shamini G**

B.Tech Information Technology

Vellore Institute of Technology (VIT), Vellore

---

## ⭐ Conclusion

This project introduces a novel Environmental-Clinical Hybrid Risk Scoring (ECHRS) framework that enhances thyroid disease prediction by integrating medical and environmental factors. The proposed approach provides a more personalized and interpretable risk assessment than traditional binary classification systems, supporting earlier identification of individuals who may benefit from preventive healthcare interventions.
