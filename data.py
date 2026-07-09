from pathlib import Path
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).parent / "Proliferation_Master Sheet_Sept 2024.xlsx"


@st.cache_data
def load_data():

    df = pd.read_excel(
        DATA_PATH,
        sheet_name="Full Data Set"
    )

    df.columns = (
        df.columns.astype(str)
        .str.strip()
    )

    return df
