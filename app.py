from numpy import datetime64
from pandas_datareader import data as pdr
import streamlit as st

import yfinance as yf
from datetime import date

yf.pdr_override() # <== that's all it takes :-)

# download yahoo finance data to dataframe
ticker= 'VGT'

data = pdr.get_data_yahoo(ticker, start="2021-01-01", end=date.today())

st.dataframe(data)
st.caption('VGT This is caption')