import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import os
import datetime as dt

def plot_csv(file):
    month_numbers = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    matplotlib.use('qtagg')
    with open(f"data/{file}") as f:
        reader = csv.reader(f)
        data = [row for row in reader][3:]


    x = [dt.datetime.strptime(row[1].replace(row[1][:3], str(month_numbers.index(row[1][:3]) + 1)).replace('  ', ' '),'%m %d %Y').date() for row in data]
    y = [int(row[2]) for row in data]

    plt.plot(x, y)
    plt.xlabel('Date')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=180))
    plt.ylabel('Cases')
    plt.gcf().autofmt_xdate()
    plt.savefig(f'static/{file[:-4]}.svg')