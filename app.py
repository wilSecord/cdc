import tkinter as tk
from tkinter import ttk
import csv
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image, ImageTk
import datetime as dt
import re
import os

app = tk.Tk()

geographies = []
data_types = []

for item in os.listdir('data/csv/'):
    data_types.append(re.findall('\D*__', item)[0][15:-2].replace('_', ' ').title())
    geographies.append(re.findall('__\D*.csv', item)[0][2:-4].replace('_', ' ').title())

geographies = sorted(list(set(geographies)))
data_types = sorted(list(set(data_types)))


def main():
    app.geometry('640x640')

    startup_location_1 = tk.StringVar(app)
    startup_location_1.set(geographies[0])
    location_1 = ttk.Combobox(app, values=geographies)
    location_1.grid(column=0, row=0)

    startup_options_1 = tk.StringVar(app)
    startup_options_1.set(data_types[0])
    option_1 = ttk.Combobox(app, values=data_types)
    option_1.grid(column=1, row=0)

    startup_location_2 = tk.StringVar(app)
    startup_location_2.set(geographies[0])
    location_2 = ttk.Combobox(app, values=geographies)
    location_2.grid(column=0, row=1)

    startup_options_2 = tk.StringVar(app)
    startup_options_2.set(data_types[0])
    option_2 = ttk.Combobox(app, values=data_types)
    option_2.grid(column=1, row=1)

    # def graph():
    #     plot_csv(f'data_table_for_{opt_1_choice.lower().replace(" ", "_")}__{loc_1_choice.lower().replace(" ", "_")}.csv',
    #              f'data_table_for_{opt_2_choice.lower().replace(" ", "_")}__{loc_2_choice.lower().replace(" ", "_")}.csv')
    #     img = Image.open('data/graph.png')
    #     display = ImageTk.PhotoImage(img)
    #     label = tk.Label(app, image=display)
    #     label.grid(column=1, row=2, columnspan=3)

    def plot_csv():
        # fig = Figure()
        loc_1_choice = location_1.get()
        opt_1_choice = option_1.get()
        loc_2_choice = location_2.get()
        opt_2_choice = option_2.get()
        file = f'data_table_for_{opt_1_choice.lower().replace(" ", "_")}__{loc_1_choice.lower().replace(" ", "_")}.csv'
        file2 = f'data_table_for_{opt_2_choice.lower().replace(" ", "_")}__{loc_2_choice.lower().replace(" ", "_")}.csv'

        month_numbers = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        dates = ['Nov 30 2022', 'Nov 23 2022', 'Nov 16 2022', 'Nov  9 2022', 'Nov  2 2022', 'Oct 26 2022', 'Oct 19 2022', 'Oct 12 2022', 'Oct  5 2022', 'Sep 28 2022', 'Sep 21 2022', 'Sep 14 2022', 'Sep  7 2022', 'Aug 31 2022', 'Aug 24 2022', 'Aug 17 2022', 'Aug 10 2022', 'Aug  3 2022', 'Jul 27 2022', 'Jul 20 2022', 'Jul 13 2022', 'Jul  6 2022', 'Jun 29 2022', 'Jun 22 2022', 'Jun 15 2022', 'Jun  8 2022', 'Jun  1 2022', 'May 25 2022', 'May 18 2022', 'May 11 2022', 'May  4 2022', 'Apr 27 2022', 'Apr 20 2022', 'Apr 13 2022', 'Apr  6 2022', 'Mar 30 2022', 'Mar 23 2022', 'Mar 16 2022', 'Mar  9 2022', 'Mar  2 2022', 'Feb 23 2022', 'Feb 16 2022', 'Feb  9 2022', 'Feb  2 2022', 'Jan 26 2022', 'Jan 19 2022', 'Jan 12 2022', 'Jan  5 2022', 'Dec 29 2021', 'Dec 22 2021', 'Dec 15 2021', 'Dec  8 2021', 'Dec  1 2021', 'Nov 24 2021', 'Nov 17 2021', 'Nov 10 2021', 'Nov  3 2021', 'Oct 27 2021', 'Oct 20 2021', 'Oct 13 2021', 'Oct  6 2021', 'Sep 29 2021', 'Sep 22 2021', 'Sep 15 2021', 'Sep  8 2021', 'Sep  1 2021', 'Aug 25 2021', 'Aug 18 2021', 'Aug 11 2021', 'Aug  4 2021', 'Jul 28 2021', 'Jul 21 2021', 'Jul 14 2021', 'Jul  7 2021', 'Jun 30 2021', 'Jun 23 2021', 'Jun 16 2021', 'Jun  9 2021', 'Jun  2 2021', 'May 26 2021', 'May 19 2021', 'May 12 2021', 'May  5 2021', 'Apr 28 2021', 'Apr 21 2021', 'Apr 14 2021', 'Apr  7 2021', 'Mar 31 2021', 'Mar 24 2021', 'Mar 17 2021', 'Mar 10 2021', 'Mar  3 2021', 'Feb 24 2021', 'Feb 17 2021', 'Feb 10 2021', 'Feb  3 2021', 'Jan 27 2021', 'Jan 20 2021', 'Jan 13 2021', 'Jan  6 2021', 'Dec 30 2020', 'Dec 23 2020', 'Dec 16 2020', 'Dec  9 2020', 'Dec  2 2020', 'Nov 25 2020', 'Nov 18 2020', 'Nov 11 2020', 'Nov  4 2020', 'Oct 28 2020', 'Oct 21 2020', 'Oct 14 2020', 'Oct  7 2020', 'Sep 30 2020', 'Sep 23 2020', 'Sep 16 2020', 'Sep  9 2020', 'Sep  2 2020', 'Aug 26 2020', 'Aug 19 2020', 'Aug 12 2020', 'Aug  5 2020', 'Jul 29 2020', 'Jul 22 2020', 'Jul 15 2020', 'Jul  8 2020', 'Jul  1 2020', 'Jun 24 2020', 'Jun 17 2020', 'Jun 10 2020', 'Jun  3 2020', 'May 27 2020', 'May 20 2020', 'May 13 2020', 'May  6 2020', 'Apr 29 2020', 'Apr 22 2020', 'Apr 15 2020', 'Apr  8 2020', 'Apr  1 2020', 'Mar 25 2020', 'Mar 18 2020', 'Mar 11 2020', 'Mar  4 2020', 'Feb 26 2020', 'Feb 19 2020', 'Feb 12 2020', 'Feb  5 2020', 'Jan 29 2020']
        matplotlib.use('tkagg')

        with open(f"data/csv/{file}") as f:
            reader = csv.reader(f)
            data = [row for row in reader][3:]

        y = [row[2] for row in data]

        with open(f"data/csv/{file2}") as f:
            reader = csv.reader(f)
            data = [row for row in reader][3:]

        y1 = [row[2] for row in data]

        for i in range(len(dates)):
            if y[i] == 'N/A' or y1[i] == 'N/A':
                dates[i] = ''
                y[i] = ''
                y1[i] = ''

        y = [int(number) for number in y if number]
        y1 = [int(number) for number in y1 if number]

        dates = [date for date in dates if date]
        x = [dt.datetime.strptime(row.replace(row[:3], str(month_numbers.index(row[:3]) + 1)).replace('  ', ' '), '%m %d %Y').date() for row in dates]

        types = [re.findall('\D*__', item)[0][15:-2].replace('_', ' ').title() for item in [file, file2]]
        geographies = [re.findall('__\D*.csv', item)[0][2:-4].replace('_', ' ').title() for item in [file, file2]]

        plt.title(f'{geographies[0]} {types[0]} vs {geographies[1]} {types[1]}', loc='left')
        loc1, = plt.plot(x, y, label=loc_1_choice)
        loc2, = plt.plot(x, y1, label=loc_2_choice)
        plt.legend(handles=[loc1, loc2])
        plt.xlabel('Date')
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=180))
        plt.ylabel('Cases')
        plt.gcf().autofmt_xdate()
        plt.savefig('data/graph.png')
        plt.cla()

        img = Image.open('data/graph.png')
        tk_img = ImageTk.PhotoImage(img)

        label = tk.Label(app, image=tk_img)
        label.image = tk_img
        label.grid(row=2, column=0, columnspan=3)

        os.remove('data/graph.png')

    graph_button = tk.Button(app, text='Show Graph', command=plot_csv)
    graph_button.grid(column=2, row=1)

if __name__ == '__main__':
    main()
    app.mainloop()