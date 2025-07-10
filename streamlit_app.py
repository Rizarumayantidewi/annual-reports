import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# =========================
# SETUP HALAMAN & LOGO
# =========================
st.set_page_config(page_title="Alfamart BSC Dashboard", layout="wide")
st.title("📊 Alfamart Balanced Scorecard Dashboard (2021–2024)")
st.title("by : Riza Rumayanti Dewi")
# Load logo
logo = Image.open("/workspaces/bsc4/data/logo-alfa.jpg")  # Ubah ke path logo kamu
st.image(logo, width=150)

# =========================
# DATA PREPARATION
# =========================

# HRM (Learning & Growth)
hrm_data = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024],
    "Average_Training_Hours": [50.37, 54.61, 76.56, 38.88],
    "Turnover_Rate": [None, None, None, 2.83],
    "Appraisal_Percentage": [None, None, None, 90.16]
})

# Customer
customer_data = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024],
    "NPS": [None, None, None, 85.82],
    "Customer_Complaints": [3916, 3420, 5184, 7146],
    "Resolution_Percentage": [100, 100, 92, 95],
    "CSAT": [None, None, 86.08, None]
})

# Internal Process
internal_data = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024],
    "Inventory_Turnover": [8.20, 8.60, 8.30, 8.49],
    "DSI": [44.51, 42.44, 43.90, 43.00],
    "Receivables_Turnover": [48.39, 49.39, 45.20, 42.49]
})

# Financial
financial_data = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024],
    "Revenue_Million_Rp": [84904, 96925, 106945, 118227],
    "Net_Profit_Million_Rp": [1989, 2907, 3484, 3220],
    "Net_Profit_Margin": [2.34, 3.00, 3.26, 2.66],
    "ROE": [22.09, 25.38, 22.19, 20.41],
    "EPS": [47.9, 69.9, 81.97, 77.6]
})

# =========================
# SIDEBAR NAVIGASI
# =========================
menu = st.sidebar.radio("📂 Pilih Perspektif:", [
    "1️⃣ HRM (Learning & Growth)",
    "2️⃣ Customer",
    "3️⃣ Internal Business Process",
    "4️⃣ Financial"
])

# =========================
# HRM DASHBOARD
# =========================
if menu.startswith("1️⃣"):
    st.header("💼 HRM (Learning & Growth) Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("📘 Avg. Training Hours (2024)", f"{hrm_data['Average_Training_Hours'][3]} jam")
    col2.metric("🔁 Turnover Rate (2024)", f"{hrm_data['Turnover_Rate'][3]} %")
    col3.metric("✅ Appraisal Coverage (2024)", f"{hrm_data['Appraisal_Percentage'][3]} %")

    st.subheader("📈 Trend Rata-rata Jam Pelatihan")
    chart = alt.Chart(hrm_data).mark_line(point=True, color="#035AA6").encode(
        x="Year:O", y="Average_Training_Hours:Q"
    ).properties(height=300)
    st.altair_chart(chart, use_container_width=True)

# =========================
# CUSTOMER DASHBOARD
# =========================
elif menu.startswith("2️⃣"):
    st.header("🛒 Customer Perspective Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("💬 NPS (2024)", "85.82")
    col2.metric("📉 Total Keluhan (2024)", f"{customer_data['Customer_Complaints'][3]}")
    col3.metric("✅ Penyelesaian Keluhan (2024)", f"{customer_data['Resolution_Percentage'][3]} %")

    st.subheader("📊 Tren Keluhan Pelanggan")
    chart = alt.Chart(customer_data).mark_bar(color="#ED1F21").encode(
        x="Year:O", y="Customer_Complaints:Q"
    ).properties(height=300)
    st.altair_chart(chart, use_container_width=True)

# =========================
# INTERNAL PROCESS DASHBOARD
# =========================
elif menu.startswith("3️⃣"):
    st.header("🏭 Internal Business Process Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("🔁 Inventory Turnover (2024)", f"{internal_data['Inventory_Turnover'][3]}")
    col2.metric("🗓️ DSI (2024)", f"{internal_data['DSI'][3]} hari")
    col3.metric("💰 Receivables Turnover (2024)", f"{internal_data['Receivables_Turnover'][3]}")

    st.subheader("📈 Inventory Turnover Over Time")
    chart = alt.Chart(internal_data).mark_line(point=True, color="#FCD413").encode(
        x="Year:O", y="Inventory_Turnover:Q"
    ).properties(height=300)
    st.altair_chart(chart, use_container_width=True)

# =========================
# FINANCIAL DASHBOARD
# =========================
elif menu.startswith("4️⃣"):
    st.header("💵 Financial Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("📈 Total Revenue (2024)", f"{financial_data['Revenue_Million_Rp'][3]:,} M")
    col2.metric("💰 Net Profit (2024)", f"{financial_data['Net_Profit_Million_Rp'][3]:,} M")
    col3.metric("📊 Net Profit Margin (2024)", f"{financial_data['Net_Profit_Margin'][3]}%")

    st.subheader("📈 Revenue vs Net Profit")
    chart = alt.Chart(financial_data).transform_fold(
        ['Revenue_Million_Rp', 'Net_Profit_Million_Rp'],
        as_=['KPI', 'Value']
    ).mark_line(point=True).encode(
        x='Year:O',
        y='Value:Q',
        color='KPI:N'
    ).properties(height=300)
    st.altair_chart(chart, use_container_width=True)

    st.subheader("📉 ROE dan EPS")
    chart2 = alt.Chart(financial_data).transform_fold(
        ['ROE', 'EPS'],
        as_=['Metric', 'Value']
    ).mark_bar().encode(
        x='Year:O',
        y='Value:Q',
        color='Metric:N'
    ).properties(height=300)
    st.altair_chart(chart2, use_container_width=True)
