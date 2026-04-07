# 🔄 Pipeline Walkthrough

## 1. Data Extraction
- Python script calls job API
- Response is saved as JSON

Why?
- Raw data is preserved for reprocessing
- APIs are unreliable, so we store a backup

---

## 2. Data Processing (PySpark)

We load JSON into Spark:

```python
spark.read.option("multiline", "true").json("data/jobs.json")
