import yfinance as yf
import talib as ta
import pandas as pd

def get_data(crypto):
  df = yf.download(crypto, start="2020-01-01", end="2021-02-15")
  return df

df1 = get_data("BTC-USD")
df2 = get_data("ETH-USD")
df3 = get_data("BNB-USD")
df4 = get_data("DOGE-USD")
df5 = get_data("DOT1-USD")
df6 = get_data("ADA-USD")
df7 = get_data("LINK-USD")
df8 = get_data("USDT-USD")
df9 = get_data("XRP-USD")
df10 = get_data("LTC-USD")
df11 = get_data("BCH-USD")
df12 = get_data("XLM-USD")
df13 = get_data("XMR-USD")
df14 = get_data("NEO-USD")
df15 = get_data("DASH-USD")
df16 = get_data("USDC-USD")
df17 = get_data("MIOTA-USD")
df18 = get_data("XTZ-USD")

def get_MOM(data):
  data["momentum"]  = ta.MOM(data["Close"], timeperiod=7)
  return data.momentum.iat[-1]

def get_RSI(data):
  data["rsi"] = ta.RSI(data["Close"], timeperiod=7)
  return data.rsi.iat[-1]

def get_macd(data):
  data["macd"], data["macdsignal"], data["macdhist"] = ta.MACD(data["Close"], fastperiod=12, slowperiod=26, signalperiod=9)

def get_price(data):
  return data.Close.iat[-1]

def get_slowk(data):
  data["slowk"], data["slowd"] = ta.STOCH(data["High"], data["Low"], data["Close"], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
  return data.slowk.iat[-1]

def get_slowd(data):
  data["slowk"], data["slowd"] = ta.STOCH(data["High"], data["Low"], data["Close"], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
  return data.slowd.iat[-1]

dataframes = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18]

for dataframe in dataframes:

  dataframe.RSI = get_RSI(dataframe)
  dataframe.MOM= get_MOM(dataframe)
  dataframe.price = get_price(dataframe)
  dataframe.macd = get_macd(dataframe)
  
  if dataframe.RSI<=60 and dataframe.MOM <0:
    dataframe.decision = "Buy"
  elif dataframe.RSI>=85 and dataframe.MOM >0:
    dataframe.decision = "Sell"
  else:
    dataframe.decision = "Hold/No action"

data = {'Crytpocurrency':  ['BTC-USD', 'ETH-USD', 'BNB-USD', 'DOGE-USD', 'DOT1-USD', 'ADA-USD', 'LINK-USD', 'USDT-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD', 'XLM-USD', 'XMR-USD', 'NEO-USD', 'DASH-USD', 'USDC-USD', 'MIOTA-USD', 'XTZ-USD' ],
        'Price': [df1.price, df2.price, df3.price, df4.price, df5.price, df6.price, df7.price, df8.price, df9.price, df10.price, df11.price, df12.price, df13.price, df14.price, df15.price, df16.price, df17.price, df18.price],
        'RSI': [df1.RSI, df2.RSI, df3.RSI, df4.RSI, df5.RSI, df6.RSI,df7.RSI, df8.RSI, df9.RSI, df10.RSI, df11.RSI, df12.RSI, df13.RSI, df14.RSI, df15.RSI, df16.RSI, df17.RSI, df18.RSI],
        'Momentum' : [df1.MOM, df2.MOM, df3.MOM, df4.MOM, df5.MOM, df6.MOM, df7.MOM, df8.MOM, df9.MOM, df10.MOM, df11.MOM, df12.MOM, df13.MOM, df14.MOM, df15.MOM, df16.MOM, df17.MOM, df18.MOM],
        'Decision' : [df1.decision, df2.decision, df3.decision, df4.decision, df5.decision, df6.decision, df7.decision, df8.decision, df9.decision, df10.decision, df11.decision, df12.decision, df13.decision, df14.decision, df15.decision, df16.decision, df17.decision, df18.decision]
        }

dfinal = pd.DataFrame (data, columns = ['Crytpocurrency','Price','RSI', 'Momentum', 'Decision'])

dfinal

