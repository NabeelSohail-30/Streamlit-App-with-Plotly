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


# data management
year_option = df['year'].unique().tolist()
year = st.selectbox("which year should we plot?", year_option, 0)

# plotting

fig = px.scatter(df, x= 'gdpPercap', y ='lifeExp', size='pop', color='continent', hover_name='continent',
                log_x=True, size_max=55, range_x=[100,100000], range_y=[20,90],
                animation_frame='year', animation_group='country')
                

fig.update_layout(width=800, height=600)

st.write(fig)         
