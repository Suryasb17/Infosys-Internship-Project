import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('SBI.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

plt.figure(figsize=(10,5))
plt.plot(df.index, df['Open'], label='Opening Peice')
plt.xlabel('Date')
plt.ylabel('Opening Price')
plt.title('Stock Market Direction')
plt.legend()
plt.grid()
plt.show()
