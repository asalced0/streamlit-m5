# Import streamlit and pandas.
import streamlit as st
import pandas as pd

# Print title.
st.title('Streamlit con cache')

# Set dataset url.
DATA_URL = 'dataset.csv'

@st.cache
def load_data(nrows):
    # Create dataframe data, con n rows.
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # Return dataframe.
    return data

# Print text loading data...
data_load_state = st.text('Loading data...')

# Call function load_data.
data = load_data(1000)

# Print text done...
data_load_state.text("Done !")

# Print dataframe.
st.dataframe(data)