import pandas as pd
import matplotlib.pyplot as plt
import calendar as cal

file = r'Budget_data'
plt.style.use('seaborn')
lim = 11

money_table = pd.read_csv(file, sep=',', parse_dates=[4])

money_table.groupby('category').sum().plot.pie(subplots=True, legend=False, autopct='%1.0f%%')
plt.ylabel('')
explode = []
for i in range(len(money_table['payee'].value_counts())):
    explode.append(0)
# explode[-1] = 0.2
# explode[-2] = 0.1
shops = money_table.groupby('payee').sum().sort_values(by=['price'], ascending=False)
lab = shops.index

shops[:lim].plot.pie(subplots=True, legend=False,  autopct='%1.0f%%', explode=explode[:lim], labels=lab)
plt.ylabel('')
# money_table['day'] = money_table['date'].dt.day
money_table['Month'] = money_table['date'].dt.month
money_table['Month'] = money_table['Month'].apply(lambda x: cal.month_abbr[x])
# money_table['year'] = money_table['date'].dt.year
ax = money_table.groupby('Month').sum().plot.bar(subplots=False, legend=False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.spines['left'].set_visible(False)
ax.grid(axis='x')
plt.xlabel('')
plt.ylabel('')
# dramas_id = (a['genres'].str.contains('Horror', na=False) &
#               a['titleType'].str.contains('movie', na=False) &
#               a['isAdult'].str.contains('1', na=False))
# dramas = a[dramas_id]
# counts = dramas['startYear'].value_counts()[0:20].plot(kind='bar')

plt.show()