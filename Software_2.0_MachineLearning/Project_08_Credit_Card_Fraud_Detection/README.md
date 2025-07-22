# Project 08 – Credit Card Fraud Detection

## 📄 Project Description
This project implements a machine learning pipeline to detect fraudulent credit card transactions, addressing the challenges of class imbalance and precision-critical classification.

## 🎯 Objectives
- Handle imbalanced datasets effectively
- Engineer meaningful features for fraud detection
- Train robust classifiers
- Optimize for precision-recall over accuracy

## 🛠️ Tools & Technologies
Python, Pandas, Scikit-learn, XGBoost, Matplotlib, Seaborn, Imbalanced-learn (SMOTE)

## 📊 Dataset
- Source: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Contains anonymized transaction features and binary fraud labels

## 🔍 Key Steps
1. Data Preprocessing
2. Addressing Class Imbalance using SMOTE
3. Model Training with Random Forest, XGBoost
4. Evaluation using Precision-Recall, ROC Curve
5. Feature Importance Analysis

## ✅ Results
- Best Model: XGBoost
- Precision: 0.91 | Recall: 0.83
- Key Insight: Only ~0.17% of transactions were fraudulent, necessitating high recall sensitivity

## 📌 Takeaways
- Demonstrated handling of highly imbalanced classification tasks
- Emphasized cost-sensitive metrics relevant in real-world fraud systems
- Built foundations for real-time fraud alert systems
