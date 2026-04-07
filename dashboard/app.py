import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("📊 Job Market Data Platform")

# Connect to database
engine = create_engine("sqlite:///jobs.db")

# Load data
df = pd.read_sql("SELECT * FROM jobs", engine)

st.subheader("Raw Data")
st.dataframe(df)

# Location distribution
st.subheader("Jobs by Location")
location_counts = df["candidate_required_location"].value_counts()
st.bar_chart(location_counts)

# Company distribution
st.subheader("Top Companies")
company_counts = df["company_name"].value_counts().head(10)
st.bar_chart(company_counts)
