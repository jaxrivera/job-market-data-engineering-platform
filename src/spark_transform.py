from pyspark.sql import SparkSession

def run_spark_job():
    spark = SparkSession.builder \
        .appName("JobDataProcessing") \
        .getOrCreate()

    # Load raw JSON data
    df = spark.read.option("multiline", "true").json("data/jobs.json")
    # Select relevant columns
    df_clean = df.select(
        "title",
        "company_name",
        "candidate_required_location",
        "publication_date"
    )

    # Show preview
    df_clean.show(5)

    # Save processed data
    df_clean.write.mode("overwrite").parquet("data/processed_jobs")

    spark.stop()

if __name__ == "__main__":
    run_spark_job()
