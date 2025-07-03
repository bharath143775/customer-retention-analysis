# 📦 Customer Retention Analysis

## 👋 Introduction

Imagine you’re running an online store. Every day, new customers make purchases. But after a while, some never come back.  
This project is about finding out **why customers stop returning** and **how we can retain them better**.

This repository provides a complete workflow for analyzing customer retention using Python and popular data science libraries. It includes data cleaning, exploratory analysis, statistical testing, cohort analysis, and actionable recommendations.

## 🎯 Project Goal

Our objective is simple:
- Analyze past customer behavior
- Understand what causes them to leave
- Use **data and statistics** to recommend how to keep them coming back

We don’t just want to say “X customers churned” — we want to say **why**, **when**, and **what to do next**.

## 📊 What We Did (At a Glance)

| Step | What We Explored | What We Learned |
|------|------------------|-----------------|
| 1️⃣ Descriptive Stats | Who are our customers? What do they spend? | Churned users had fewer orders and older last purchases |
| 2️⃣ Visual Analysis | Boxplots, bar charts, distributions | Easy to spot differences between churned and loyal users |
| 3️⃣ Hypothesis Testing | Are the differences real or just luck? | Order frequency significantly affects churn |
| 4️⃣ Cohort Analysis | Do new customers behave differently each month? | Yes! Some months had better retention than others |
| 5️⃣ Retention Curve | How long do people stay after joining? | Most customers drop off after the 1st or 2nd month |
| 6️⃣ A/B Testing | What works better: a reminder email or a ₹100 coupon? | Coupons improved retention by ~20% ✅ |

## 🧪 Techniques Used

- 📉 Descriptive Statistics
- 📈 Data Visualization
- 📊 Hypothesis Testing (t-test, chi-square)
- 📅 Cohort Analysis
- 🔁 Retention Curves
- 🧪 A/B Testing

## 🧠 Key Insights

- 💸 Customers with only 1 or 2 orders are 4x more likely to churn
- ⏳ Customers inactive for 60+ days are at high risk
- 🎯 ₹100 coupon improved return rate by ~20%
- 🗓️ Some cohorts had much better retention — hinting at better campaigns/offers

## 🛠 Tools Used

| Tool | Purpose |
|------|---------|
| Python (Pandas, NumPy, Seaborn, Scikit-learn, Statsmodels, Plotly, etc.) | Data cleaning, analysis, statistics, visualization |
| Jupyter Notebook | Interactive analysis and explanation |

## 📁 Folder Structure

```
customer-retention-analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── scripts/
```

- **data/raw/**: Original data files
- **data/processed/**: Cleaned and transformed data
- **notebooks/**: Jupyter notebooks for analysis
- **scripts/**: Python scripts for data processing and analysis
- **reports/visuals/**: Generated plots and reports

## 🚀 Getting Started

1. **Clone the repository**
   ```sh
   git clone https://github.com/bharath143775/customer-retention-analysis.git
   cd customer-retention-analysis
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Explore the notebooks**
   - Open the `notebooks/` folder in Jupyter and start with the main analysis notebook.

## ✅ Use Cases

- Showcase applied statistics skills
- Build retention strategy
- Extend into churn prediction or LTV modeling

## 🧑‍💻 Author

**T Bharath Kumar Reddy**  
Business Intelligence Analyst | Power BI | Python | SQL  
📅 July 2025