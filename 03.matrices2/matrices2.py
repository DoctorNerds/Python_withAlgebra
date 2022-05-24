"""
@author: Fábio Mori
"""

#Escola Matriz - Class 23: Matrices II

#Import and plot the data from file .csv using pandas and pyplot libraries
import matplotlib.pyplot as plt
import pandas as pd

BTC = pd.read_csv('BTC_1ano.csv')
plt.figure(figsize=(25,15))
#plt.title('Bitcoin Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.title('Bitcoin Prices over Time (in USD)')
plt.plot(BTC.Date, BTC.AdjClose, 'b.-', label='United States')
plt.xticks(rotation=45)
plt.xlabel('Period')
plt.ylabel('Price US Dollars')