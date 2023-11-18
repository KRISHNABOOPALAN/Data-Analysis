#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import yfinance as yf

# Step 1: Fetch EUR/INR data from Yahoo Finance
# Define the date range and currency pair
start_date = "2023-01-01"
end_date = "2023-11-02"
currency_pair = "EURINR=X"

# Download data using yfinance
data = yf.download(currency_pair, start=start_date, end=end_date)

# Step 2: Calculate technical indicators
# Moving Averages
data['SMA_5'] = data['Close'].rolling(window=5).mean()
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Bollinger Bands
window = 20
data['SMA'] = data['Close'].rolling(window=window).mean()
data['STD'] = data['Close'].rolling(window=window).std()
data['BB_upper'] = data['SMA'] + (data['STD'] * 2)
data['BB_lower'] = data['SMA'] - (data['STD'] * 2)

# CCI (Commodity Channel Index)
window = 14
tp = (data['High'] + data['Low'] + data['Close']) / 3
data['SMA_TP'] = tp.rolling(window=window).mean()
data['CCI'] = (tp - data['SMA_TP']) / (0.015 * tp.rolling(window=window).std())

# Step 3: Decision making
# Define the analysis date for one day
one_day_analysis_date = input("Enter the START-date for analysis (e.g., 2023-11-02):")
# Define the analysis date for one week
one_week_analysis_date =input("Enter the END-date for analysis (e.g., 2023-11-02):")

# Check if the specified dates are in the dataset
if one_day_analysis_date in data.index and one_week_analysis_date in data.index:
    one_day_analysis_data = data[data.index == one_day_analysis_date]
    one_week_analysis_data = data[data.index == one_week_analysis_date]

    # Check conditions for one day and one week
    one_day_condition = one_day_analysis_data['SMA_5'].values[0] > one_day_analysis_data['SMA_20'].values[0]
    one_week_condition = one_week_analysis_data['SMA_5'].values[0] > one_week_analysis_data['SMA_20'].values[0]

    # Determine the decisions
    one_day_decision = "BUY" if one_day_condition else "SELL"
    one_week_decision = "BUY" if one_week_condition else "SELL"

    print(f"One-Day Decision for {one_day_analysis_date}: {one_day_decision}")
    print(f"One-Week Decision for {one_week_analysis_date}: {one_week_decision}")
else:
    print("One or both analysis dates are not available in the dataset.")


# In[22]:


import pandas as pd
import yfinance as yf
import plotly.express as px

# Step 1: Fetch EUR/INR data from Yahoo Finance
# Define the date range and currency pair
start_date = "2023-01-01"
end_date = "2023-11-02"
currency_pair = "EURINR=X"

# Download data using yfinance
data = yf.download(currency_pair, start=start_date, end=end_date)

# Create a line chart to compare EUR/INR exchange rates over time
fig = px.line(data, x=data.index, y="Close", title=f'EUR/INR Exchange Rate ({start_date} to {end_date})')
fig.update_layout(yaxis_title='EUR/INR Exchange Rate')
fig.update_xaxes(title_text='Date')
fig.show()


# In[21]:


import pandas as pd
import yfinance as yf
import plotly.express as px

# Step 1: Fetch EUR/INR data from Yahoo Finance
# Define the date range and currency pair
start_date =input("Enter the start-date for analysis (e.g., 2023-11-02):")
end_date = input("Enter the end-date for analysis (e.g., 2023-11-02):")
currency_pair = "EURINR=X"

# Download data using yfinance
data = yf.download(currency_pair, start=start_date, end=end_date)

# Calculate the percentage change in the EUR/INR exchange rate
data['PercentageChange'] = data['Close'].pct_change() * 100

# Create a line chart to visualize the percentage change over time
fig = px.line(data, x=data.index, y="PercentageChange", title=f'Percentage Change in EUR/INR Exchange Rate ({start_date} to {end_date})')
fig.update_layout(yaxis_title='Percentage Change')
fig.update_xaxes(title_text='Date')
fig.show()


# In[20]:


import pandas as pd
import yfinance as yf
import plotly.express as px

# Step 1: Fetch EUR/INR data from Yahoo Finance
# Define the date range and currency pair
start_date = "2023-01-01"
end_date = "2023-11-02"
currency_pair = "EURINR=X"

# Download data using yfinance
data = yf.download(currency_pair, start=start_date, end=end_date)

# Calculate 5-day and 20-day moving averages
data['SMA_5'] = data['Close'].rolling(window=5).mean()
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Create a line chart to visualize the moving averages over time
fig = px.line(data, x=data.index, y=["Close", "SMA_5", "SMA_20"], 
title=f'EUR/INR Exchange Rate and Moving Averages ({start_date} to {end_date})')
fig.update_layout(yaxis_title='Exchange Rate')
fig.update_xaxes(title_text='Date')
fig.show()


# In[26]:


import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

# Step 1: Fetch EUR/INR data from Yahoo Finance
# Define the date range and currency pair
start_date = "2023-01-01"
end_date = "2023-11-02"
currency_pair = "EURINR=X"

# Download data using yfinance
data = yf.download(currency_pair, start=start_date, end=end_date)

# Calculate Bollinger Bands
window = 20
data['SMA'] = data['Close'].rolling(window=window).mean()
data['STD'] = data['Close'].rolling(window=window).std()
data['BB_upper'] = data['SMA'] + (data['STD'] * 2)
data['BB_lower'] = data['SMA'] - (data['STD'] * 2)

# Create a Bollinger Bands graph
fig = go.Figure()

# Add the EUR/INR closing prices as a line
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='EUR/INR'))

# Add Bollinger Bands as shaded areas
fig.add_trace(go.Scatter(x=data.index, y=data['BB_upper'], fill=None, mode='lines', line_color='red', name='BB Upper'))
fig.add_trace(go.Scatter(x=data.index, y=data['BB_lower'], fill='tonexty', mode='lines', line_color='blue', name='BB Lower'))

# Update layout
fig.update_layout(title=f'Bollinger Bands for EUR/INR ({start_date} to {end_date})',
                  xaxis_title='Date',
                  yaxis_title='EUR/INR Exchange Rate',
                  showlegend=True)

fig.show()


# In[27]:


import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

# Step 1: Fetch EUR/INR data from Yahoo Finance
# Define the date range and currency pair
start_date = "2023-01-01"
end_date = "2023-11-02"
currency_pair = "EURINR=X"

# Download data using yfinance
data = yf.download(currency_pair, start=start_date, end=end_date)

# Calculate CCI (Commodity Channel Index)
window = 14
tp = (data['High'] + data['Low'] + data['Close']) / 3
data['SMA_TP'] = tp.rolling(window=window).mean()
data['CCI'] = (tp - data['SMA_TP']) / (0.015 * tp.rolling(window=window).std())

# Create a CCI graph
fig = go.Figure()

# Add the CCI values as a line
fig.add_trace(go.Scatter(x=data.index, y=data['CCI'], mode='lines', name='CCI'))

# Add threshold lines for overbought and oversold levels (typically +100 and -100)
fig.add_shape(type='line', x0=data.index[0], x1=data.index[-1], y0=100, y1=100, line=dict(color='red', width=2), name='Overbought (100)')
fig.add_shape(type='line', x0=data.index[0], x1=data.index[-1], y0=-100, y1=-100, line=dict(color='green', width=2), name='Oversold (-100)')

# Update layout
fig.update_layout(title=f'Commodity Channel Index (CCI) for EUR/INR ({start_date} to {end_date})',
                  xaxis_title='Date',
                  yaxis_title='CCI Value',
                  showlegend=True)

fig.show()

