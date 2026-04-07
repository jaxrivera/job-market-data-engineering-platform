# ⚠️ Common Errors & Fixes

## 1. ModuleNotFoundError: requests
### Cause:
Missing dependency in virtual environment

### Fix:

pip install requests


2. Spark JVM error (UnsupportedClassVersionError)
Cause:

Java version mismatch with Spark

Fix:
Installed Java 17
Set correct JAVA_HOME
Matched Spark compatibility
3. PySpark _corrupt_record issue
Cause:

Spark couldn't parse JSON array properly

Fix:
.option("multiline", "true")
4. Java gateway exited error
Cause:

Incorrect Java setup or version mismatch

Fix:
Reconfigured Java alternatives
Ensured correct version selection
5. Streamlit not showing data
Cause:

Incorrect database path or missing table

Fix:
Verified SQLite DB exists
Confirmed table creation via Spark pipeline

---

# 🚀 HOW TO CREATE THESE FILES

Run:
mkdir docs
nano docs/1_project_overview.md

Repeat for each file.
