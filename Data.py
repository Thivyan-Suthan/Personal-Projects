import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
st.set_page_config(page_title='Automated Dashboard')
st.title('Match Rate')
st.write('First visualisation')

def scatter_vis(x):
    boxplot=sns.boxplot(data=x,x='A')
    
    return boxplot

def lineplot(x):
    line=px.line(x,x='A',y='B')

    return line 

#col=st.columns((2,1,1))
col1, col2 = st.columns([2,1])


with col1:
    st.header('scatter graph')
    scatter=scatter_vis(df)
    data=scatter
    st.pyplot(data.figure)

with col2:
    st.header('line graph')
    line=lineplot(df)
    data=line
    fig=go.Figure(data)
    fig.show()
    

