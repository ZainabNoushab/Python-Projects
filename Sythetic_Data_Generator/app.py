import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ---------------------------
# Helpers: Synthetic Generators
# ---------------------------
def generate_numeric(n, mean=50.0, std=10.0, decimals=2):
    data = np.random.normal(mean, std, n)
    return np.round(data, decimals)

def generate_categorical(n, categories=None):
    cats = categories or ["A", "B", "C", "D"]
    cats = [c.strip() for c in cats if c.strip()]
    if not cats:
        cats = ["A", "B", "C", "D"]
    return [random.choice(cats) for _ in range(n)]

def generate_text(n, length=8):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ["".join(random.choices(alphabet, k=length)) for _ in range(n)]

def generate_dates(n, start_date="2020-01-01", end_date="2023-12-31"):
    start = datetime.strptime(str(start_date), "%Y-%m-%d")
    end = datetime.strptime(str(end_date), "%Y-%m-%d")
    span_days = (end - start).days
    if span_days < 0:
        start, end = end, start
        span_days = (end - start).days
    return [start + timedelta(days=random.randint(0, span_days)) for _ in range(n)]

# ---------------------------
# Streamlit App
# ---------------------------
st.set_page_config(page_title="Synthetic Data Generator", layout="centered")
st.title("📊 Synthetic Data Generator (SDG)")
st.caption("Add columns, generate synthetic rows, preview and download CSV.")

# Persist the schema while the user interacts
if "columns" not in st.session_state:
    st.session_state.columns = []   # each item: {"name", "type", "params"}

# Controls
num_rows = st.number_input("Rows to generate", min_value=10, max_value=1_000_000, value=100, step=50)

with st.expander("➕ Add a column", expanded=True):
    with st.form("add_col_form", clear_on_submit=True):
        col_name = st.text_input("Column name", value="col1")
        col_type = st.selectbox("Column type", ["Numeric", "Categorical", "Text", "Date"])

        params = {}
        if col_type == "Numeric":
            mean = st.number_input("Mean", value=50.0)
            std = st.number_input("Std Dev", value=10.0, min_value=0.0)
            decimals = st.number_input("Decimals", value=2, min_value=0, max_value=6, step=1)
            params = {"mean": float(mean), "std": float(std), "decimals": int(decimals)}

        elif col_type == "Categorical":
            cats = st.text_input("Categories (comma-separated)", value="A,B,C")
            params = {"categories": [c.strip() for c in cats.split(",")]}

        elif col_type == "Text":
            length = st.number_input("Length of random string", value=8, min_value=1, max_value=40, step=1)
            params = {"length": int(length)}

        elif col_type == "Date":
            start_date = st.date_input("Start date", value=datetime(2020, 1, 1))
            end_date = st.date_input("End date", value=datetime(2023, 12, 31))
            params = {"start_date": str(start_date), "end_date": str(end_date)}

        add_btn = st.form_submit_button("Add column")
        if add_btn:
            if not col_name.strip():
                st.warning("Please provide a column name.")
            else:
                st.session_state.columns.append({"name": col_name.strip(), "type": col_type, "params": params})
                st.success(f"Added: {col_name} ({col_type})")

# Show current schema
st.subheader("Current schema")
if st.session_state.columns:
    st.dataframe(
        pd.DataFrame([
            {
                "name": c["name"],
                "type": c["type"],
                "params": str(c["params"])
            } for c in st.session_state.columns
        ])
    )
    cols1, cols2 = st.columns(2)
    if cols1.button("🧹 Clear all columns"):
        st.session_state.columns = []
        st.toast("Cleared schema.", icon="🧽")
    if cols2.button("✨ Add example schema"):
        st.session_state.columns.extend([
            {"name": "price", "type": "Numeric", "params": {"mean": 100.0, "std": 15.0, "decimals": 2}},
            {"name": "category", "type": "Categorical", "params": {"categories": ["A", "B", "C"]}},
            {"name": "sku", "type": "Text", "params": {"length": 10}},
            {"name": "order_date", "type": "Date", "params": {"start_date": "2022-01-01", "end_date": "2024-12-31"}},
        ])
        st.toast("Example schema added.", icon="✅")
else:
    st.info("No columns yet. Use **Add a column** above.")

# Generate data
st.subheader("Generate")
if st.button("🚀 Generate synthetic data"):
    if not st.session_state.columns:
        st.warning("Please add at least one column.")
    else:
        data = {}
        for c in st.session_state.columns:
            name, ctype, p = c["name"], c["type"], c["params"]
            if ctype == "Numeric":
                data[name] = generate_numeric(num_rows, **p)
            elif ctype == "Categorical":
                data[name] = generate_categorical(num_rows, **p)
            elif ctype == "Text":
                data[name] = generate_text(num_rows, **p)
            elif ctype == "Date":
                data[name] = generate_dates(num_rows, **p)

        df = pd.DataFrame(data)
        st.success(f"Generated dataset with shape {df.shape}.")
        st.dataframe(df.head(20), use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="synthetic_data.csv", mime="text/csv")
