import pandas as pd
from sqlalchemy import create_engine

def load_to_warehouse():
    # Read Spark output
    df = pd.read_parquet("data/processed_jobs")

    # Create SQLite database
    engine = create_engine("sqlite:///jobs.db")

    # Load into table
    df.to_sql("jobs", engine, if_exists="replace", index=False)

    print("Data loaded into jobs.db")

if __name__ == "__main__":
    load_to_warehouse()
