# import libraries
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Interactive Data Visualization with Plotly")

# Create a selectbox to choose an in-built dataset
selected_dataset = st.selectbox("Select a Dataset", ["Iris", "Tips", "Wind", "GapMinder"])

# Define a dictionary to map dataset names to corresponding functions
dataset_functions = {
    "Iris": px.data.iris,
    "Tips": px.data.tips,
    "GapMinder": px.data.gapminder,
    "Wind": px.data.wind,
}

# Load the selected dataset
if selected_dataset in dataset_functions:
    df = dataset_functions[selected_dataset]()
else:
    st.error("Invalid dataset selection. Please choose a valid dataset.")

# Display the dataset summary
st.write(f"## {selected_dataset} Dataset")
st.write(df)

st.write(f"## {selected_dataset} Columns")
st.write(df.columns)

st.write(f"## {selected_dataset} Summary")
st.write(df.describe())

# Create a sidebar for user input
st.sidebar.header("Plot Configuration")

# User input for plot data
x_axis = st.sidebar.selectbox("X-Axis", df.columns)
y_axis = st.sidebar.selectbox("Y-Axis", df.columns)
color = st.sidebar.selectbox("Color", df.columns)
size = st.sidebar.selectbox("Size", df.columns)
hover = st.sidebar.selectbox("Hover Name", df.columns)
animation = st.sidebar.selectbox("Animation Frame", df.columns)
animation_grp = st.sidebar.selectbox("Animation Group", df.columns)

# Check if the selected size column is numeric
if size in df.select_dtypes(include=["number"]).columns:
    # Only proceed if size is a numeric column
    st.write("### Plot")

    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        size=size,
        color=color,
        hover_name=hover,
        log_x=True,
        size_max=55,
        range_x=[100, 100000],
        range_y=[20, 90],
        animation_frame=animation,
        animation_group=animation_grp,
    )

    fig.update_layout(width=800, height=600)

    st.plotly_chart(fig)
else:
    st.warning(f"'{size}' is not a numeric column in the dataset. Please choose a valid numeric column for 'Size'.")

# Add a footer with credits and data source information
st.markdown(
    """
*Data source: [Plotly Express Datasets](https://plotly.com/python-api-reference/generated/plotly.express.data.html)*
*Built with Streamlit and Plotly*
"""
)
