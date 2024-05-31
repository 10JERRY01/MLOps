#Using yahoo finance to see the stock prices of Microsoft using streamlit between fixed dates.

import streamlit as st
import yfinance as yf

msft = yf.Ticker("MSFT")
hist = msft.history(period='1d', start='2019-01-01', end='2023-01-01')
st.write(
    """
        # This app shows MSFT stock hist and daily closing price 
    """
)
st.write(hist)

st.line_chart(hist.Close)

#Using yahoo finance to see the stock prices of Microsoft using streamlit where you can choose the date.
st.write(
    '''
        # This app shows microsoft stocks and lets you choose the dates 
    '''
)
import datetime

start_date = st.date_input("Enter start date", datetime.date(2019, 1, 1))

end_date = st.date_input("Enter end date", datetime.date(2022, 12, 31))

ticker_symbol = 'MSFT'
st.write(ticker_symbol)
ticker_date = yf.Ticker(ticker_symbol)
ticker_df = ticker_date.history(period='1d', start=f'{start_date}', end=f'{end_date}')

st.dataframe(ticker_df)

st.write(
    """
        ## Daily Closing Price Chart
    """
)

st.line_chart(ticker_df.Close)

st.write(
    """
        ## Volume Of Shares Traded Each Day
    """
)

st.line_chart(ticker_df.Volume)