from numpy import datetime64
from pandas_datareader import data as pdr
import streamlit as st

import yfinance as yf
from datetime import date

# change the page title name
st.set_page_config(
   page_title = "simplestreamlit",
)


yf.pdr_override() # <== that's all it takes :-)

# download yahoo finance data to dataframe
ticker= 'VGT'

data = pdr.get_data_yahoo(ticker, start="2021-01-01", end=date.today())

st.dataframe(data)
st.caption('VGT This is caption')


col1, col2 = st.columns(2)

with col1:
    col1.header("Original")
    st.write ('This column 1')

with col2:
    col2.header("Grayscale")
    st.write ('This is column 2')

