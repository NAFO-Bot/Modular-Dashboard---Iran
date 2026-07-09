import streamlit as st
from data import load_data
from metrics import render_sidebar
from globe import render_globe
from network import render_network
from analysis import render_analysis
from sources import render_sources

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Iranian Drone Proliferation Dashboard",
    page_icon="🇮🇷",
    layout="wide"
)

st.title("🇮🇷 Iranian Drone Proliferation Dashboard")
st.caption(
    "Interactive Open-Source Intelligence Dashboard for Historical Iranian UAV Proliferation"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

try:
    df = load_data()

except Exception as e:
    st.error(f"Unable to load dataset.\n\n{e}")
    st.stop()

# --------------------------------------------------
# Normalize Column Names
# --------------------------------------------------

df.columns = (
    df.columns
      .astype(str)
      .str.strip()
)

# --------------------------------------------------
# Filter to Iran
# --------------------------------------------------

filtered = (
    df[
        df["Supplier"]
        .astype(str)
        .str.strip()
        .eq("Iran")
    ]
    .copy()
)

if filtered.empty:
    st.warning("No Iranian export records found.")
    st.stop()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

render_sidebar(filtered)

# --------------------------------------------------
# Tabs
# --------------------------------------------------
tab_globe, tab_network, tab_analysis, tab_data, tab_sources = st.tabs(
    [
        "🌍 Globe",
        "🕸 Network",
        "📊 Analysis",
        "📄 Data",
        "📚 Sources"
    ]
)

# --------------------------------------------------
# Globe
# --------------------------------------------------

with tab_globe:
    render_globe(filtered)

# --------------------------------------------------
# Network
# --------------------------------------------------

with tab_network:
    render_network(filtered)

# --------------------------------------------------
# Analysis
# --------------------------------------------------

with tab_analysis:
    render_analysis(filtered)

# --------------------------------------------------
# Dataset
# --------------------------------------------------

with tab_data:

    st.subheader("Filtered Dataset")

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )
with tab_sources:
    render_sources()
st.caption(
    "© 2026 Sagnik Nath • Iranian Drone Proliferation Dashboard • Open-Source Intelligence Visualization"
)
