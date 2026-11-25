
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Automotive Supply Chain AI",
    page_icon="🚗",
    layout="wide"
)

st.title("Automotive Supply Chain AI")
st.write(
    "AI-powered demand forecasting and inventory "
    "optimization for automotive manufacturing."
)

# Load existing project outputs
output_folder = Path("outputs")

forecast_file = output_folder / "demand_forecast.csv"
inventory_file = output_folder / "inventory_recommendations.csv"
supplier_file = output_folder / "supplier_performance.csv"

# Demand Forecast
st.subheader("Demand Forecast")

if forecast_file.exists():
    forecast = pd.read_csv(forecast_file)
    st.dataframe(forecast, use_container_width=True)
else:
    st.warning("Demand forecast file is not available.")

# Inventory Recommendations
st.subheader("Inventory Recommendations")

if inventory_file.exists():
    inventory = pd.read_csv(inventory_file)
    st.dataframe(inventory, use_container_width=True)
else:
    st.warning("Inventory recommendations are not available.")

# Supplier Performance
st.subheader("Supplier Performance")

if supplier_file.exists():
    supplier = pd.read_csv(supplier_file)
    st.dataframe(supplier, use_container_width=True)
else:
    st.warning("Supplier performance file is not available.")
