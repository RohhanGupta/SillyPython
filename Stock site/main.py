import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

st.markdown('''
# Rohan's Stock Price Potral
Shown are the stock price data for query companies!
''')
st.write('---')

st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

choice= ['Companies','Crypto']
tradechoice = st.sidebar.selectbox('Pick Your trade', choice)
if(tradechoice=='Companies'):
    stock_list = pd.read_csv('nse_companies.csv')
    stockSymbol = st.sidebar.selectbox('Pick Your Company', stock_list) 
    stockData = yf.Ticker(stockSymbol)
    stockDf = stockData.history(period='1d', start=start_date, end=end_date)
elif(tradechoice=='Crypto'):
    crypto_list = pd.read_csv('r.csv')
    cryptoSymbol = st.sidebar.selectbox('Pick Your Company', crypto_list)
    cryptoData = yf.Ticker(cryptoSymbol)
    cryptokDf = cryptoData.history(period='1d', start=start_date, end=end_date)

string_logo = '<img src=%s>' % stockData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = stockData.info['longName']
st.header('**%s**' % string_name)

string_sector = stockData.info['sector']
st.write("Company Sector - " + string_sector)

string_summary = stockData.info['longBusinessSummary']
st.info(string_summary)

# Data Representation Tabular
st.header('**Stock data**')
st.write(stockDf)

# Data Representation Graphical
st.header('**Stock Graph**')
qf=cf.QuantFig(stockDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)