import streamlit as st
import networkx as nx
from pyvis.network import Network
import os
import tempfile

st.set_page_config(page_title="Network Visualization", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
        .navbar {
            background-color: #007BFF;
            overflow: hidden;
            padding: 10px 20px;
            text-align: center;
            border-radius: 10px;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            padding: 12px 20px;
            display: inline-block;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
        }
        .navbar a:hover {
            background-color: #0056b3;
            border-radius: 8px;
        }
        .main-header {
            font-size: 2.5em;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .content-section {
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="navbar">
        <a href="#">Home</a>
        <a href="#">Data</a>
        <a href="#">Network</a>
    </div>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">Nomological Network of Behavioral Medicine</p>', unsafe_allow_html=True)

st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.subheader("Overview")
st.write("This visualization represents a network of dimensions related to Behavioral Medicine. Each node is a dimension, and connections indicate relationships between them.")
st.image("https://via.placeholder.com/800x400", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.subheader("Static Data")
st.write("Here is a sample dataset representing some nodes and their relationships:")

data = {
    "Nodes": ["Dim 961: Caregiving", "Dim 826: Duration", "Dim 523: Reality Affirmation", "Dim 644: Self-Injury"],
    "Connections": [
        ("Dim 961", "Dim 826"),
        ("Dim 826", "Dim 523"),
        ("Dim 523", "Dim 644"),
        ("Dim 644", "Dim 961")
    ]
}

st.write(data)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.subheader("Graph Visualization")

G = nx.Graph()
for node in data["Nodes"]:
    G.add_node(node)

for edge in data["Connections"]:
    G.add_edge(*edge)

with tempfile.TemporaryDirectory() as tmpdirname:
    network_html_path = os.path.join(tmpdirname, "network_graph.html")

    net = Network(height="500px", width="100%", notebook=False, bgcolor="#f8f9fa", font_color="black")
    net.from_nx(G)
    net.save_graph(network_html_path)

    with open(network_html_path, "r", encoding="utf-8") as f:
        html_code = f.read()

    st.components.v1.html(html_code, height=550)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("© 2025 Research Group | Behavioral Medicine Network", unsafe_allow_html=True)
