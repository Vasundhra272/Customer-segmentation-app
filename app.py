import streamlit as st
import pandas as pd
import pickle

# Load saved model and scaler
with open("rfm_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("🛒 Customer Segmentation App")
st.write("Upload customer RFM data and predict which segment they belong to.")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    data = pd.read_csv(uploaded_file)

    st.subheader("📂 Uploaded Data")
    st.dataframe(data.head())

    # Scale the RFM values
    rfm_scaled = scaler.transform(data[["Recency", "Frequency", "Monetary"]])

    # Predict clusters
    clusters = kmeans.predict(rfm_scaled)

    # Map clusters to meaningful names
    cluster_labels = {
        0: "High Value Customers",
        1: "Churn Risk",
        2: "Loyal Customers"
    }

    # Add predictions to the dataframe
    data["Cluster"] = clusters
    data["Segment"] = data["Cluster"].map(cluster_labels)

    st.subheader("🔎 Segmented Customers")
    st.dataframe(data)

    # Show cluster distribution with labels
    st.subheader("📊 Cluster Distribution")
    st.bar_chart(data["Segment"].value_counts())
