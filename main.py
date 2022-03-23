import talib
import yfinance
import pandas
import flask

data = yfinance.download('^BSESN',start='2021-06-01',end='2021-06-18')
#print(data)

morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])
engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
doji = talib.CDLDOJI(data['Open'], data['High'], data['Low'], data['Close'])

data['morning_star'] = morning_star
data['engulfing'] = engulfing
data['doji'] = doji

engulfing_days = data[data['engulfing']!=0]
morning_star_days = data[data['morning_star']!=0]
doji_days = data[data['doji']!=0]

print('Morning Star Days -> \n')
print(morning_star_days)
print('\n\n\nEngulfing Days -> \n')
print(engulfing_days)
print('\n\n\nDoji Days -> \n')
print(doji_days)


tick = yfinance.Ticker("^BSESN")
print(tick.history(start='2021-06-01',end='2021-06-18'))