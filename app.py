import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title("Plotly examples")
st.markdown("Um markdown, pequenino")
st.sidebar.title('Aqui temos um título provavelmente maneiro')
url= 'coord-ita.csv'
@st.cache(persist=True)
def load_data():
  data= pd.read_csv(url)
  return data
data= load_data()   
st.write(data)
st.sidebar.subheader("Isso  um subheader")
random_tweet = st.sidebar.radio('Sentiment',('Fazenda Penedo','Jambeiro','Maringá'))
st.sidebar.markdown(data.query('Bairro==@random_tweet')['Bairro'].sample(n=1).values[0])
select=st.sidebar.selectbox('tipo de visualização',('Histogram','Pie chart'),key='1')
if not st.sidebar.checkbox('Hide',True):
    st.markdown('ta acontecendo:')
    if select == 'Histogram':
        fig= px.bar({'Sentiment':['positive','neutral','negative'],'Tweets':[
        20,30,40
        ]},x='Sentiment',y='Tweets',color='Tweets',height=500)
        st.plotly_chart(fig)
    else:
        fig=px.pie({'Sentiment':['positive','neutral','negative'],'Tweets':[
        20,30,40]},values='Tweets',names='Sentiment')
        st.plotly_chart(fig)
