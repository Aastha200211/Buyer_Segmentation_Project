🏠 Machine Learning Based Buyer Segmentation and Investment Profiling for Real Estate Market Intelligence

📌 Project Overview

This project focuses on segmenting real estate buyers using Machine Learning (K-Means Clustering). The goal is to analyze customer demographics, property transactions, and purchasing behavior to identify different buyer groups and provide insights that support targeted marketing and investment decisions.

An interactive Streamlit dashboard was developed to visualize buyer segments, property sales, and customer insights.

---

🎯 Problem Statement

Real estate companies generate large amounts of customer and transaction data. Analyzing this data manually is difficult and time-consuming. This project uses Machine Learning to group buyers into meaningful segments, helping businesses understand customer behavior and make data-driven decisions.

---

🚀 Features

- Data Cleaning and Preprocessing
- Feature Engineering (Age, Year, Month)
- K-Means Clustering
- Elbow Method for Optimal Clusters
- Silhouette Score Evaluation
- Buyer Segmentation
- Interactive Streamlit Dashboard
- KPI Cards
- Interactive Filters
- Data Visualization
- Download Filtered Data

---

📂 Dataset

The project uses two datasets:

Client Dataset
- Client ID
- Client Type
- Name
- Gender
- Date of Birth
- Country
- Region
- Satisfaction Score
- Loan Applied
- Referral Channel

Property Dataset
- Listing ID
- Transaction Date
- Unit Category
- Floor Area
- Sale Price
- Listing Status
- Client Reference

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Git & GitHub

---

🤖 Machine Learning Model

Algorithm Used:
- K-Means Clustering

Model Evaluation:
- Elbow Method
- Silhouette Score

Buyer Segments Identified:
- Budget Buyers
- Mid-Range Investors
- Premium Home Buyers
- Luxury Investors
- Young Premium Buyers

---

📊 Dashboard Features

- Dashboard Overview
- Buyer Segment Distribution
- Average Sale Price Analysis
- Average Buyer Age
- Satisfaction Score Analysis
- Buyer Analysis Scatter Plot
- Interactive Filters
- Buyer Details Table
- Download CSV Feature

---

📈 Key Insights

- Budget Buyers represent the largest customer segment.
- Luxury Investors purchase the highest-value properties.
- Premium Home Buyers have high customer satisfaction.
- Buyer segmentation helps businesses create targeted marketing strategies.
- Interactive dashboards improve business decision-making.

---

📁 Project Structure

```
Buyer_Segmentation_Project/
│
├── app.py
├── Buyer_Segmentation.ipynb
├── buyer_segmentation_final.csv
├── cleaned_data.csv
├── clients.csv
├── properties.csv
├── background.png
├── requirements.txt
└── README.md
```

---

⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Aastha200211/Buyer_Segmentation_Project.git
```

Go to the project folder:

```bash
cd Buyer_Segmentation_Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

🌐 Live Demo

**Streamlit App**

https://buyersegmentationproject.streamlit.app/

---

📚 Future Scope

- Predict buyer purchasing behavior using classification models.
- Integrate real-time property listings.
- Add advanced analytics and forecasting.
- Deploy using cloud platforms with a connected database.

---

👩‍💻 Developed By

**Aastha Sapate**
---



