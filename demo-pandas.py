# Import streamlit.
import streamlit as st
import pandas as pd

names_link = 'dataset.csv'

# Read csv.
names_data = pd.read_csv(names_link)

# Create title.
st.title('Pandas - Dataframe')

# Print dataframe.
st.dataframe(names_data)