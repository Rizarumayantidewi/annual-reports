import streamlit as st
import pandas as pd
import altair as alt

# Set halaman
st.set_page_config(page_title="Alfamart BI Dashboard", page_icon="📊")

# Tambahkan logo Alfamart (teks + garis)
# Tambahkan ini sebelum st.title()
logo_html = """
<div style="text-align:center; padding-top: 10px;">
    <h1 style="margin-bottom: 0; font-size: 36px;">
        <span style="color:#035AA6; font-weight: bold;">Alfa</span>
        <span style="color:#ED1F21; font-style:italic; font-weight: bold;">mart</span>
    </h1>
    <div style="height:6px; width:200px; margin:auto; background-color:#ED1F21; border-radius:3px;"></div>
    <div style="height:6px; width:200px; margin:auto; background-color:#FCD413; border-radius:3px; margin-top:2px;"></div>
</div>
"""
st.markdown(logo_html, unsafe_allow_html=True)

# Judul halaman
st.title("📊 KPI FINANCIAL DASHBOARD — ALFAMART")
st.markdown("By: **Riza Rumayanti Dewi** | NIM: 20240130015 | MI24M")
st.markdown("---")

# Data KPI
data = {
    "Year": [2021, 2022, 2023, 2024],
    "Revenue": [84904301000, 96924686000, 106944683000, 118227031000],
    "Net_Profit": [1988750000, 2907478000, 3484025000, 3220083000],
    "Gross_Margin": [20.83, 20.66, 21.57, 21.45],
    "Operating_Margin": [3.31, 3.89, 4.14, 3.45],
    "Net_Margin": [2.34, 3.00, 3.26, 2.72],
    "ROE": [22.09, 25.38, 22.19, 18.21],
    "EPS": [0.0479, 0.0699, 0.08197, 0.0776],
    "YOY_Growth": [11.00, 14.88, 10.43, 10.55],
    "Total_Expenses": [83055990000, 94126025000, 103658852000, 115245135000]
}

df = pd.DataFrame(data)

# ============================
# 📌 TOP SECTION – KPI METRICS
# ============================
st.subheader("📌 KPI Snapshot by Year")
st.dataframe(df, use_container_width=True)

# ===============================
# 📈 MIDDLE SECTION – TRENDS
# ===============================

col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 Revenue vs Net Profit (2021–2024)")
    revenue_profit_chart = alt.Chart(df).transform_fold(
        ['Revenue', 'Net_Profit'],
        as_=['Metric', 'Value']
    ).mark_line(point=True).encode(
        x='Year:O',
        y='Value:Q',
        color='Metric:N'
    ).properties(height=300)
    st.altair_chart(revenue_profit_chart, use_container_width=True)

with col2:
    st.subheader("📉 Profit Margins Over Time")
    margin_chart = alt.Chart(df).transform_fold(
        ['Gross_Margin', 'Net_Margin'],
        as_=['Margin_Type', 'Value']
    ).mark_area(opacity=0.6).encode(
        x='Year:O',
        y='Value:Q',
        color='Margin_Type:N'
    ).properties(height=300)
    st.altair_chart(margin_chart, use_container_width=True)

# =========================================
# 📊 BOTTOM SECTION – FINANCIAL RATIOS
# =========================================

col3, col4 = st.columns(2)
with col3:
    st.subheader("📊 ROE and EPS Over Time")
    roe_eps_chart = alt.Chart(df).transform_fold(
        ['ROE', 'EPS'],
        as_=['Metric', 'Value']
    ).mark_bar().encode(
        x='Year:O',
        y='Value:Q',
        color='Metric:N'
    ).properties(height=300)
    st.altair_chart(roe_eps_chart, use_container_width=True)

with col4:
    st.subheader("🧾 Total Expenses (Triliun Rupiah)")
    st.bar_chart(df.set_index("Year")[["Total_Expenses"]]/1e12)

# ============================
# ✅ FOOTER / PENJELASAN
# ============================

with st.expander("📌 Penjelasan Analisis KPI"):
    st.markdown("""
    **1. Revenue & Net Profit:** terus meningkat dari 2021–2023, namun Net Profit menurun di 2024 meskipun Revenue tetap naik.
    
    **2. Profit Margins:** Gross dan Net Margin cenderung stabil, dengan Gross di atas 20% dan Net di kisaran 2–3%.

    **3. Return on Equity (ROE):** Menurun di tahun 2024 (18,2%) setelah puncaknya di 2022 (25,4%).

    **4. EPS:** Bertumbuh sampai 2023 (Rp0,08197), lalu sedikit menurun di 2024 menjadi Rp0,0776.

    **5. Total Expenses:** Sejalan dengan pertumbuhan Revenue, naik hingga Rp115 triliun pada 2024.
    """)

st.caption("📅 Data sumber: Laporan Tahunan Alfamart 2021–2024 | Dibuat oleh Riza Rumayanti Dewi 💼")
