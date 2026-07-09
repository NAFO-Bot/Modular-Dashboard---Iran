import streamlit as st


def render_sources():

    st.title("📚 Sources & Methodology")

    st.markdown("""
This dashboard visualizes historical transfers of Iranian unmanned aerial systems (UAS) using publicly available information.

The objective of this application is to support exploratory analysis of historical proliferation patterns. It is intended for research, education, and open-source intelligence (OSINT) visualization.

---

## Primary Data Sources

- United Nations Panel of Experts reports
- SIPRI Arms Transfers Database
- Military Balance (IISS)
- Open-source reporting
- Government publications
- Defence journalism and investigative reporting

---

## Dataset

The dataset records historical export events and includes attributes such as:

- Supplier
- Recipient
- Platform Model
- Year of First Delivery
- Region

It was published by CNAS and the project was headed by Molly Campbell. Records were standardized, cleaned and geocoded for visualization.

---

## Visualizations

- 🌍 Interactive Globe
- 🕸 Network Graph
- 📊 Statistical Analysis
- 📄 Dataset Explorer

---

## Methodology

1. Collect open-source records.
2. Validate recipient and platform information.
3. Standardize country names.
4. Assign geographic coordinates.
5. Build an interactive analytical dashboard using Streamlit and Plotly.

---

## Limitations

This dashboard reflects publicly reported historical transfer events.

Open-source reporting may be incomplete, delayed, or revised over time. The absence of a transfer record should not be interpreted as evidence that no transfer occurred.

This application does not model operational capability, battlefield effectiveness, inventory levels, or current force posture.

---

## Disclaimer

This project is an independent analytical visualization built using publicly available information.

It is intended solely for research, education, and analytical purposes.
""")