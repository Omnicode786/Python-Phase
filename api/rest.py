# REST APIs: These enable communication over the internet, where your program acts as a client. The API interacts with a web service, following specific rules for requests and responses, typically using HTTP methods and JSON files.
from pycoingecko import CoinGeckoAPI
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.offline as pyo


os.chdir(r"E:\Programming\Google  Python\Python-Phase\api")
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id="bitcoin",vs_currency="usd",days=30)

#  this repsonse inb a json fileexressed as a dictionary
# print(bitcoin_data['prices'])

data = pd.DataFrame(bitcoin_data['prices'], columns=['Timestamp','Price'])
print(data)
data["Date"] = pd.to_datetime(data["Timestamp"], unit='ms')

# print(data)

# del data["Timestamp"]
# print(data)


#  the best way to delete a column is to use the drop method
# df = df.drop('column_name', axis=1)

# data = data.drop("Timestamp", axis=1)


# where 1 is the axis number (0 for rows and 1 for columns.)

# data["Price"] = data["Price"].round().astype(int)

# print(data)
# data.to_csv("bitcoindata.csv", index=False)
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price':['min','max','first','last']})






fig = go.Figure(data=[go.Candlestick(x = candlestick_data.index,open = candlestick_data['Price']['first'],
                                                  high = candlestick_data['Price']['max'],
                                                  low = candlestick_data['Price']['min'],
                                                  close = candlestick_data['Price']['last'])
                                                  ])


fig.update_layout(xaxis_rangeslider_visible = False, xaxis_title = 'Date', 
                  yaxis_title = 'Price (USD $)', title = "Bitcoin Candlestick chart over 30 days")

pyo.offline.plot(fig, filename = './bitcoing.html',auto_open = True)