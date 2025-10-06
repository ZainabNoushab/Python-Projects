# 🛍️ Customer Segmentation using K-Means Clustering
---
## 📘 Overview

This project applies K-Means Clustering, an unsupervised machine learning algorithm, to segment customers based on their Annual Income and Spending Score. The goal is to help businesses understand their customer base better and develop targeted marketing strategies.

---
## 🚀 Project Objective

To identify different groups of customers (clusters) based on purchasing behavior and income levels using data-driven segmentation.

---
### 🧠 Key Steps

#### Data Collection:
Imported the Mall_Customers.csv dataset containing demographic and spending information of mall customers.

#### Data Preprocessing:
Selected the last two columns (Annual Income and Spending Score) for clustering.

#### Elbow Method:
Calculated the Within Cluster Sum of Squares (WCSS) to determine the optimal number of clusters.

#### Model Training:
Applied K-Means Clustering to divide customers into 5 distinct groups.

#### Visualization:
Visualized clusters using Matplotlib and Seaborn to interpret customer segments clearly.

---
## 🧩 Technologies Used

Python

NumPy

Pandas

Matplotlib

Seaborn

Scikit-learn

---
## 📊 Results

The model successfully identifies 5 distinct customer clusters based on spending patterns and income:

Cluster 1: High Income, High Spending

Cluster 2: Average Income, Average Spending

Cluster 3: Low Income, Low Spending

Cluster 4: High Income, Low Spending

Cluster 5: Low Income, High Spending

---
## 🧾 Dataset

**Source:** [Mall Customers Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

**Features Used:**

Annual Income (k$)

Spending Score (1–100)

---
## 🧰 How to Run

#### Clone this repository:

```bash
git clone https://github.com/ZainabNoushab/Customer_Segmentation.git
```

#### Run the script:

```bash
python customer_segmentation.py
```

---
## 💡 Insights

Businesses can use this segmentation to target promotions and tailor experiences.

High-value customers can be rewarded with loyalty benefits.

Low-income high-spending groups can be analyzed for credit or affordability risks.

---
## 🏁 Conclusion

K-Means clustering provides a simple yet powerful approach to customer segmentation. This analysis gives a clear view of different customer types, helping organizations optimize their marketing and business strategies.

---
## ✨ Author

Zainab Noushab

📧 [Email](znoushab@gmail.com)

💼 [LinkedIn Profile](www.linkedin.com/in/zainab-noushab)
