import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker

frame = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv",
                    parse_dates=['Date'])
countries = ['India', 'US', 'China']
frame = frame[frame['Country'].isin(countries)]

frame['Cases'] = frame[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

frame = frame.pivot(index="Date", columns="Country", values="Cases")
countries = list(frame.columns)
covid = frame.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries
populations = {'India': 1352642280, 'US': 330548815, 'China': 1438027228}
percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country] / populations[country] * 100000

colors = {'India':'#045275', 'China':'#089099','US':'#DC3977'}
plt.style.use('fivethirtyeight')

plot = covid.plot(figsize=(12,8), color=list(colors.values()), linewidth=5, legend=False)
plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')

for country in list(colors.keys()):
    plot.text(x = covid.index[-1], y = covid[country].max(), color = colors[country], s = country, weight = 'bold')


