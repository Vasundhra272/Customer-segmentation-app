# 🛒 Customer Segmentation App

This project is a **Streamlit web app** for customer segmentation using **RFM analysis (Recency, Frequency, Monetary)**.  
The app allows you to upload customer transaction data, applies a pre-trained KMeans clustering model, and predicts which customer segment they belong to.

---

## 🚀 Features
- Upload a CSV file with customer RFM data
- Automatically scales the data using a pre-trained `StandardScaler`
- Predicts customer segments using a pre-trained **KMeans model**
- Displays:
  - Uploaded data preview
  - Clustered data with segment labels
  - Cluster distribution chart

---

## 🗂️ Project Structure
customer-segmentation-app/
│── app.py # Streamlit app
│── rfm_model.pkl # Saved KMeans model
│── scaler.pkl # Saved StandardScaler
│── requirements.txt # Python dependencies
│── README.md # Project documentation

🌐 Deployment

This app is deployed on Streamlit Cloud.
You can try it here: 👉 [Live Demo](https://customer-segmentation-app-t3engyahu3dgavmmzjctkh.streamlit.app/)
