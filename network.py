import os
import tempfile

import networkx as nx
from pyvis.network import Network

import streamlit as st
from streamlit.components.v1 import html


REGION_COLORS = {
    "Africa": "#2ECC71",
    "Europe": "#3498DB",
    "Middle East": "#9B59B6",
    "Asia": "#F39C12",
    "Americas": "#1ABC9C",
}


def render_network(df):
    """
    Render the PyVis proliferation network.

    Supplier
        ↓
    Platform
        ↓
    Recipient
    """

    st.subheader("🌐 Proliferation Network")

    if df.empty:
        st.warning("No records found.")
        return

    G = nx.Graph()

    # ------------------------------------------------
    # Supplier Node
    # ------------------------------------------------
    supplier = "Iran"

    G.add_node(
        supplier,
        color="#E74C3C",
        size=60,
        shape="dot",
        title=f"<b>{supplier}</b><br>Supplier",
    )

    # ------------------------------------------------
    # Build Network
    # ------------------------------------------------

    for _, row in df.iterrows():

        platform = str(
            row["Paltform Model"]
        ).strip()

        recipient = str(
            row["Seeker"]
        ).strip()

        region = str(
            row.get("Region ", "")
        ).strip()

        year = row.get(
            "Year of First Delivery",
            ""
        )

        node_color = REGION_COLORS.get(
            region,
            "#95A5A6"
        )

        # Platform node

        G.add_node(
            platform,
            color="#F39C12",
            shape="box",
            title=f"""
            <b>{platform}</b>
            <br>Platform
            """
        )

        # Recipient node

        G.add_node(
            recipient,
            color=node_color,
            shape="dot",
            title=f"""
            <b>{recipient}</b>
            <br>Region: {region}
            """
        )

        # Supplier → Platform

        G.add_edge(
            supplier,
            platform,
            color="#AAAAAA"
        )

        # Platform → Recipient

        G.add_edge(
            platform,
            recipient,
            title=f"""
            Platform: {platform}<br>
            Recipient: {recipient}<br>
            Region: {region}<br>
            First Delivery: {year}
            """,
            color="#666666"
        )

    # ------------------------------------------------
    # Node Sizes
    # ------------------------------------------------

    degree = dict(
        G.degree()
    )

    for node in G.nodes():

        G.nodes[node]["size"] = (
            degree[node] * 4
        ) + 12

    # Keep supplier large

    G.nodes[supplier]["size"] = 60

    # ------------------------------------------------
    # PyVis Network
    # ------------------------------------------------

    net = Network(
        height="900px",
        width="100%",
        bgcolor="#FFFFFF",
        font_color="black",
        directed=False,
    )

    net.from_nx(G)

    net.repulsion(
        node_distance=220,
        spring_length=250,
        spring_strength=0.05,
        central_gravity=0.15,
        damping=0.09,
    )

    net.toggle_physics(True)

    # ------------------------------------------------
    # Save temporary HTML
    # ------------------------------------------------

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".html"
    ) as tmp:

        html_path = tmp.name

    net.save_graph(html_path)

    with open(
        html_path,
        "r",
        encoding="utf-8"
    ) as f:

        source = f.read()

    html(
        source,
        height=920,
        scrolling=True,
    )

    os.remove(html_path)

    # ------------------------------------------------
    # Quick Stats
    # ------------------------------------------------

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Nodes",
        G.number_of_nodes()
    )


    # ------------------------------------------------
    # Legend
    # ------------------------------------------------

    st.markdown(
        """
