from requests.api import options
import streamlit as st
import pandas as pd 
import yfinance as yf 
import datetime
import numpy as np 
from pandas_datareader import data as pdr
import cufflinks as cf
from pathlib import Path 
import statsmodels
import matplotlib.pyplot as plt


def main():
    # App title
    st.markdown('''
    # Cryptos & Stocks  📈
   
    ''')
    st.write('------')

    # App sidebar
    st.sidebar.subheader('Parameters')
    start_date= st.sidebar.date_input('Start date', datetime.date(2020,1,1))
    end_date= st.sidebar.date_input('End date', datetime.date.today())


    # Download selected tickers from yahoo finance data to dataframe
    ticker_str= 'BTC-USD', 'ETH-USD', 'DOGE-USD', 'AAPL', 'SPYG', 'SPYD', 'VGT', 'FB'

    @st.cache
    def load_data(tickers, start_dt, end_dt):
        """
        Download stcok history data from Yahoo Finance

        Parameters:
            tickers : string
                The string of stocks
            start_dt : date
                The start date for the stock history
            end_dt : date
                The end date for the sotck history
			
        """
       
        yf_df = yf.download(ticker_str, group_by='Ticker', start= start_dt, end= end_dt)
        yf_df = yf_df.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
     
        return yf_df


    # select the ticker to display
    data= load_data(ticker_str, start_date, end_date)
    ticker_selected= st.selectbox('Select a ticker', options= ticker_str)
    s_data= data[data['Ticker']==ticker_selected]
    st.write(s_data.describe())


    # text for key take away
    # bbs= Path('BollingerBands.md').read_text()


    # # Bollinger bands
    # st.info('Bollinger Bands®')
    # st.write('Key Take Away')
    # st.markdown(bbs, unsafe_allow_html= True)

    qf= cf.QuantFig(s_data, title= 'Bollinger bands', legend= 'top', name= ticker_selected)
    qf.add_bollinger_bands()
    fig= qf.iplot(asFigure= True)
    st.plotly_chart(fig)


    st.line_chart(s_data['Close'])
    st.bar_chart(s_data['Volume'])

    

if __name__ =='__main__':
    main()

