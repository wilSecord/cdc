# Third party imports
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Standard library imports
import csv
import datetime as dt
import re
import os

# Initializing tkinter application
app = tk.Tk()

# Initializing data needed for plotting
geographies = []
data_types = []

# Getting the data from the csv files (not utilizing list comprehension to improve readability)
for item in os.listdir('data/csv/'):
    # Spread out the steps for readability

    # Grabbing regex for the data type and geography
    # ex. data_table_for_total_cases__alabama.csv
    dt_regex = re.findall(r'\D*__', item)[0]  # Guaranteed one find per search, so grabbed 0th index
    g_regex = re.findall(r'__\D*.csv', item)[0]

    # Formats by slicing off unneeded characters, replacing underscores with spaces and capitalizing
    dt_formatted = dt_regex[15:-2].replace('_', ' ').title()
    g_formatted = g_regex[2:-4].replace('_', ' ').title()

    # Appended formatted data type and geography to plot data accordingly
    data_types.append(dt_formatted)
    geographies.append(g_formatted)

# Sorts and removes duplicates in data points
geographies = sorted(list(set(geographies)))
data_types = sorted(list(set(data_types)))


def main():
    """
    Initialization of variables, setting up the tkinter window, creating plot.
    """

    # Sets tkinter window size
    app.geometry('640x640')

    # Creates list of Comboboxes to grab entries later on
    combos = []

    # Creates iterable for for loop later on
    datasets = [geographies, data_types]

    # Creates 2 location and data type option dropdown boxes
    ###
    for row in range(2):  # row 0, row 1
        for column in datasets:  # geographies, data_types
            cb = ttk.Combobox(app, values=column)  # Creates ttk combobox in tk window
            cb.grid(column=datasets.index(column), row=row)  # Maps it to a grid formatted as:

            # (0, 0) (1, 0)
            # (0, 1) (1, 1)

            combos.append(cb)  # Appends to combobox list
    ###

    def plot_csv():
        """
        Generates plot and saves to png file to be loaded into tkinter via pillows ImageTk
        """

        # Sets variables for selected options in the dropdown boxes
        inputs = [selected.get() for selected in combos]

        # Reverses earlier regexing and formatting in order to grab the file for use
        file = f'data_table_for_{inputs[1].lower().replace(" ", "_")}__{inputs[0].lower().replace(" ", "_")}.csv'
        file2 = f'data_table_for_{inputs[3].lower().replace(" ", "_")}__{inputs[2].lower().replace(" ", "_")}.csv'

        # Used for indexing to quickly exchange month abbreviations for numbers
        month_numbers = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # All the csv files utilize the same dates exactly so, instead of importing them,
        # I can initialize them here which would save some time
        dates = ['Nov 30 2022', 'Nov 23 2022', 'Nov 16 2022', 'Nov  9 2022', 'Nov  2 2022', 'Oct 26 2022', 'Oct 19 2022', 'Oct 12 2022', 'Oct  5 2022', 'Sep 28 2022', 'Sep 21 2022', 'Sep 14 2022', 'Sep  7 2022', 'Aug 31 2022', 'Aug 24 2022', 'Aug 17 2022', 'Aug 10 2022', 'Aug  3 2022', 'Jul 27 2022', 'Jul 20 2022', 'Jul 13 2022', 'Jul  6 2022', 'Jun 29 2022', 'Jun 22 2022', 'Jun 15 2022', 'Jun  8 2022', 'Jun  1 2022', 'May 25 2022', 'May 18 2022', 'May 11 2022', 'May  4 2022', 'Apr 27 2022', 'Apr 20 2022', 'Apr 13 2022', 'Apr  6 2022', 'Mar 30 2022', 'Mar 23 2022', 'Mar 16 2022', 'Mar  9 2022', 'Mar  2 2022', 'Feb 23 2022', 'Feb 16 2022', 'Feb  9 2022', 'Feb  2 2022', 'Jan 26 2022', 'Jan 19 2022', 'Jan 12 2022', 'Jan  5 2022', 'Dec 29 2021', 'Dec 22 2021', 'Dec 15 2021', 'Dec  8 2021', 'Dec  1 2021', 'Nov 24 2021', 'Nov 17 2021', 'Nov 10 2021', 'Nov  3 2021', 'Oct 27 2021', 'Oct 20 2021', 'Oct 13 2021', 'Oct  6 2021', 'Sep 29 2021', 'Sep 22 2021', 'Sep 15 2021', 'Sep  8 2021', 'Sep  1 2021', 'Aug 25 2021', 'Aug 18 2021', 'Aug 11 2021', 'Aug  4 2021', 'Jul 28 2021', 'Jul 21 2021', 'Jul 14 2021', 'Jul  7 2021', 'Jun 30 2021', 'Jun 23 2021', 'Jun 16 2021', 'Jun  9 2021', 'Jun  2 2021', 'May 26 2021', 'May 19 2021', 'May 12 2021', 'May  5 2021', 'Apr 28 2021', 'Apr 21 2021', 'Apr 14 2021', 'Apr  7 2021', 'Mar 31 2021', 'Mar 24 2021', 'Mar 17 2021', 'Mar 10 2021', 'Mar  3 2021', 'Feb 24 2021', 'Feb 17 2021', 'Feb 10 2021', 'Feb  3 2021', 'Jan 27 2021', 'Jan 20 2021', 'Jan 13 2021', 'Jan  6 2021', 'Dec 30 2020', 'Dec 23 2020', 'Dec 16 2020', 'Dec  9 2020', 'Dec  2 2020', 'Nov 25 2020', 'Nov 18 2020', 'Nov 11 2020', 'Nov  4 2020', 'Oct 28 2020', 'Oct 21 2020', 'Oct 14 2020', 'Oct  7 2020', 'Sep 30 2020', 'Sep 23 2020', 'Sep 16 2020', 'Sep  9 2020', 'Sep  2 2020', 'Aug 26 2020', 'Aug 19 2020', 'Aug 12 2020', 'Aug  5 2020', 'Jul 29 2020', 'Jul 22 2020', 'Jul 15 2020', 'Jul  8 2020', 'Jul  1 2020', 'Jun 24 2020', 'Jun 17 2020', 'Jun 10 2020', 'Jun  3 2020', 'May 27 2020', 'May 20 2020', 'May 13 2020', 'May  6 2020', 'Apr 29 2020', 'Apr 22 2020', 'Apr 15 2020', 'Apr  8 2020', 'Apr  1 2020', 'Mar 25 2020', 'Mar 18 2020', 'Mar 11 2020', 'Mar  4 2020', 'Feb 26 2020', 'Feb 19 2020', 'Feb 12 2020', 'Feb  5 2020', 'Jan 29 2020']

        # Defines the matplotlib backend
        matplotlib.use('tkagg')

        # Grabs the data from file to use for y-axis
        ###
        with open(f"data/csv/{file}") as f:
            reader = csv.reader(f)  # Inits csv reader
            data = [row1 for row1 in reader][3:]  # Ignores first three rows (used for metadata and column names)

        # Ignores first two columns out of three (Geography, Date, Data) as geography and dates are already given
        y = [row1[2] for row1 in data]
        ###

        # Grabs data for second plot, same as before
        ###
        with open(f"data/csv/{file2}") as f:
            reader = csv.reader(f)
            data = [row2 for row2 in reader][3:]

        y1 = [row2[2] for row2 in data]
        ###

        # If data is not available in either graph, remove data for all datapoints and dates at that index
        # (syncs both sets and dates)
        for i in range(len(dates)):
            if y[i] == 'N/A' or y1[i] == 'N/A':
                dates[i] = ''
                y[i] = ''
                y1[i] = ''

        # Create new list of all dates that weren't removed by previous loop
        dates = [date for date in dates if date]

        # Formats all dates to be datetime objects for matplotlib parsing
        x = []
        for d in dates:
            # Gets the index + 1 of the abbreviation for the month of month_numbers
            date_str = str(month_numbers.index(d[:3]) + 1)
            #date_str= str(month_numbers.index(d[:3]) + 1)).replace('  ', ' '),
            # Formats the dates to be datetime objects
            x.append(dt.datetime.strptime(d.replace(d[:3], date_str).replace('  ', ' '), '%m %d %Y').date())

        # x = [dt.datetime.strptime(row.replace(row[:3], str(month_numbers.index(row[:3]) + 1)).replace('  ', ' '),
        #                           '%m %d %Y').date() for row in dates]

        # Sets every data point to integer if it's not an empty string
        y = [int(number) for number in y if number]
        y1 = [int(number) for number in y1 if number]

        # Plots the data and adds labels for legend
        loc1, = plt.plot(x, y, label=inputs[0])
        loc2, = plt.plot(x, y1, label=inputs[2])
        # Creates legend
        plt.legend(handles=[loc1, loc2])
        # Labels axes
        plt.xlabel('Date')
        plt.ylabel('Cases')
        # Creates x-axis plot points on an interval of 180 days for readability
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=180))
        plt.gcf().autofmt_xdate()
        # Saves figure to png file
        plt.savefig('data/graph.png')
        # Clears once saved for reuse
        plt.cla()

        # Creates ImageTk image of the graph for tkinter embedding
        img = Image.open('data/graph.png')
        tk_img = ImageTk.PhotoImage(img)

        # Creates a label that includes the image for embedding
        label = tk.Label(app, image=tk_img)
        label.image = tk_img
        label.grid(row=2, column=0, columnspan=3)

    # Creates submit button
    graph_button = tk.Button(app, text='Show Graph', command=plot_csv)
    graph_button.grid(column=2, row=1)


if __name__ == '__main__':
    main()
    # Calls the tkinter mainloop
    app.mainloop()
