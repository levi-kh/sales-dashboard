import pandas as pd
import plotly.express as px
import streamlit as st
import networkx as nx

#LOAD THE DATA
df = pd.read_excel("dataset.xlsx")

#BUILD THE DASHBOARD UI
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Data Dashboard")

#SIDEBAR FILTER
st.sidebar.header("Settings")
unique_regions = df["Region"].unique()
selected_region = st.sidebar.selectbox("Select a Region", unique_regions)

#Filter data based on sidebar choice
filtered_df = df[df["Region"] == selected_region]

#THE TREE VIEW (TREEMAP)
st.header("1. Tree-Based View (Hierarchy)")
fig_tree = px.treemap(
    filtered_df,
    path=["Category", "Sub-Category"],
    values="Sales",
    color="Profit",
    color_continuous_scale="Greens",
    title=f"Sales Hierarchy in {selected_region}"
)
st.plotly_chart(fig_tree)

#THE GRAPH VIEW (RELATIONSHIPS)
st.header("2. Graph-Based View (Relationships)")

#Logic: items bought together in the same "Order ID"
orders = filtered_df.groupby("Order ID")["Sub-Category"].apply(list)
G = nx.Graph()

for items in orders:
    if len(items) > 1:
        main_item = items[0]
        for other_item in items[1:]:
            G.add_edge(main_item, other_item)

#I did this part for the safety check. Only draw the graph if there is data
if len(G.nodes()) > 0:
    pos = nx.spring_layout(G)
    node_x, node_y, node_text = [], [], []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)

    fig_graph = px.scatter(x=node_x, y=node_y, text=node_text, title="Product Network")
    fig_graph.update_traces(marker=dict(size=25, color="orange"), textposition="top center")
    st.plotly_chart(fig_graph)
else:
    st.write("No product relationships found for this region.")

#SUMMARY METRICS
st.header("Summary Stats")

#Calculate KPIs
sales_per_item = filtered_df.groupby("Sub-Category")["Sales"].sum()
best_item = sales_per_item.idxmax()
best_val = sales_per_item.max()
worst_item = sales_per_item.idxmin()
worst_val = sales_per_item.min()

#Display metrics in 3 columns
c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
c2.metric("Best Seller", best_item, f"${best_val:,.2f}")
c3.metric("Lowest Seller", worst_item, f"${worst_val:,.2f}", delta_color="inverse")