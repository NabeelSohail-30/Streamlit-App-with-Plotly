# import libraries
import streamlit as st
import plotly.express as px
import pandas as pd


st.title("Interactive Data Visualization with Plotly")


# Create a selectbox to choose an in-built dataset
selected_dataset = st.selectbox("Select a Dataset", ["Iris", "Tips", "Wind", "GapMinder"])


# Load the selected dataset
if selected_dataset == "Iris":
    df = px.data.iris()
elif selected_dataset == "Tips":
    df = px.data.tips()
elif selected_dataset == "GapMinder":
    df = px.data.gapminder()
else:
    df = px.data.wind()


st.write(df)
st.write(df.columns)

# summary stat
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
animationGrp = st.sidebar.selectbox("Animation Group", df.columns)


# plotting
fig = px.scatter(df, x= x_axis, y =y_axis, size=size, color=color, hover_name=hover,
                log_x=True, size_max=55, range_x=[100,100000], range_y=[20,90],
                animation_frame=animation, animation_group=animationGrp)
                

fig.update_layout(width=800, height=600)

st.write(fig)