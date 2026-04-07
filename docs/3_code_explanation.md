
# 🧠 Code Explanation

## extract.py
- Calls API
- Saves raw JSON locally

Why simple?
- Extraction should be lightweight and reliable

---

## spark_transform.py
- Initializes SparkSession
- Reads JSON
- Selects relevant columns
- Writes Parquet output

Why SparkSession?
- Entry point for all Spark operations

---

## load_warehouse.py
- Reads Parquet with Pandas
- Writes to SQLite using SQLAlchemy

Why Pandas here?
- Dataset is now small after Spark processing
- Easier integration with SQL engines
