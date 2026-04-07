# 📊 Job Market Data Engineering Platform

## 🚀 Overview
An end-to-end data engineering pipeline that extracts job market data from an API, processes it using PySpark, stores it in a SQL-based data warehouse, and visualizes insights through an interactive Streamlit dashboard.

---

## 🏗️ Architecture
API → PySpark → Parquet → SQLite → Streamlit Dashboard

---

## ⚙️ Tech Stack
- Python
- PySpark (Distributed Data Processing)
- Pandas
- SQLAlchemy
- SQLite (Data Warehouse)
- Streamlit (Dashboard / BI Tool)

---

## 🔄 Data Pipeline

### 1. Extract
- Pulls job listings from external API
- Saves raw JSON data locally

### 2. Transform (Spark)
- Cleans and structures data using PySpark
- Selects key fields:
  - title
  - company_name
  - candidate_required_location
  - publication_date

### 3. Load (Warehouse)
- Stores processed data into SQLite database
- Enables SQL-based querying

### 4. Visualize
- Streamlit dashboard for:
  - Job distribution by location
  - Top hiring companies
  - Raw dataset exploration

---

## 📊 Dashboard Preview
(Add screenshot here)

---

## ▶️ How to Run

```bash
# Clone repo
git clone https://github.com/jaxrivera/job-market-data-engineering-platform.git
cd job-market-data-engineering-platform

# Create environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run pipeline
python src/extract.py
python src/spark_transform.py
python src/load_warehouse.py

# Launch dashboard
streamlit run dashboard/app.py
