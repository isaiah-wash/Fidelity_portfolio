import numpy as np 
import matplotlib.finance as mpf
import matplotlib.pyplot as plt
import matplotlib

start = (2015, 4, 1)
end = (2016, 4, 28)

quotes = mpf.quotes_historical_yahoo_ohlc('INGN', start, end)


print quotes 