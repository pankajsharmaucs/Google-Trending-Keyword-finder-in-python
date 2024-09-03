from pytrends.request import TrendReq
import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Blockchain"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

data = pytrends.interest_over_time() 
data = data.reset_index() 



fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
fig.show() 