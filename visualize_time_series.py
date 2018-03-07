# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:23:44 2018

@author: James
"""
import os
print(os.getcwd) 
#wdir='C:/Users/James/Documents/Python Data Science/Data Visualization')

# Import matplotlib.pyplot
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('stocks.csv', parse_dates=True, index_col=0)

# Plot the aapl time series in blue
plt.plot(df.AAPL, color='blue', label='AAPL')

# Plot the ibm time series in green
plt.plot(df.IBM, color='green', label='IBM')

# Plot the csco time series in red
plt.plot(df.CSCO, color='red', label='CSCO')

# Plot the msft time series in magenta
plt.plot(df.MSFT, color='magenta', label='MSFT')

# Add a legend in the top left corner of the plot
plt.legend(loc='upper left')

# Specify the orientation of the xticks
plt.xticks(rotation=60)

# Display the plot
plt.show()
plt.close()

# Plot the series in the top subplot in blue
plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001 to 2011')
plt.plot(df.AAPL, color='blue')

# Slice aapl from '2007' to '2008' inclusive: view
view = df.AAPL['2007':'2008']

# Plot the sliced data in the bottom subplot in black
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()
plt.show()
plt.close()

# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = df.AAPL['2007-11':'2008-04']

# Plot the sliced series in the top subplot in red
plt.subplot(2,1,1)
plt.plot(view, color='red')
plt.title('AAPL: Nov. 2007 to Apr. 2008')
plt.xticks(rotation=45)

# Reassign the series by slicing the month January 2008
view = df.AAPL['2008-01']

# Plot the sliced series in the bottom subplot in green
plt.subplot(2,1,2)
plt.plot(view, color='green')
plt.title('AAPL: Jan. 2008')
plt.xticks(rotation=45)

# Improve spacing and display the plot
plt.tight_layout()
plt.show()
plt.close()