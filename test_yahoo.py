import pandas as pd
from pandas import Series, DataFrame
import numpy as np
 
import matplotlib.pyplot as plt

from pandas_datareader import data, wb
from datetime import datetime
 
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
alibaba = data.DataReader('BABA', 'yahoo', start, end)

alibaba['Adj Close'].plot(legend=True, figsize=(10,4))
plt.show()

