# 📈 Goldman Sachs Stock Price Prediction (ML + Flask)

This project is an **end-to-end Machine Learning application** that predicts the **next-day closing price of Goldman Sachs stock** using historical financial data and advanced feature engineering.

The trained model is deployed using a **Flask web application**, allowing users to enter market values and get real-time predictions.

---

## 🔹 Problem Statement

Given historical stock market data of Goldman Sachs, predict the **Next Day Closing Price** using machine learning.

This is a **time-series regression** problem with strong noise, trends, and volatility.

---

## 🔹 Features Used

The model uses the following engineered features:

- Returns  
- 7-day Moving Average  
- 30-day Moving Average  
- Volatility  
- Volume Change  
- Lagged Closing Prices  
  - Close_lag_1  
  - Close_lag_2  
  - Close_lag_3  
  - Close_lag_4  
  - Close_lag_5  
  - Close_lag_7  

These features allow the model to learn **momentum, trend, and volatility patterns**.

---

## 🔹 Data Preprocessing Pipeline

The following preprocessing steps were used:

1. **Missing Value Handling**
   - Iterative Imputer (multivariate imputation)

2. **Distribution Normalization**
   - Power Transformer (Yeo-Johnson)

3. **Scaling**
   - RobustScaler (to handle financial outliers)

4. **Outlier Detection**
   - IQR method for exploratory analysis

All steps were implemented using a **Scikit-Learn Pipeline**.

---

## 🔹 Model

- **Algorithm:** Linear Regression  
- **Pipeline:**  
  Imputer → Power Transformer → Robust Scaler → Linear Regression  

---

## 🔹 Model Performance

| Metric | Value |
|------|------|
| R² Score | **0.817** |
| MAE | **40.21** |
| MSE | **3249.43** |
| RMSE | **57.00** |

This shows strong predictive ability for a volatile financial dataset.

---

## 🔹 Flask Web App

The trained model is saved as:

