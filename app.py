import streamlit as st
import pandas as pd
import numpy as np
st.title("Plotly examples")
st.sidebar.title('Aqui temos um título provavelmente maneiro')
url= 'coord-ita.csv'
@st.cache(persist=True)
def load_data():
  data= pd.read_csv(url)
  return data
data= load_data()   
st.write(data.head())
