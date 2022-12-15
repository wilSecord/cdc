# Project Goal
This project is a solo project to help compile the CDC COVID-19 data for ease of access and to make it easier to compare data from one area to another within and including the United States.
***
## Outline
In this project, I individually downloaded all the csv files for all the areas in and including the United States that was available on the cdc.gov website. 

I used python's standard library os, re, and csv imports in order to sort through this data. On top of that, I used third party libraries matplotlib, tkinter, and pillow to work with the data to create a window to select what data you want, graph it, and display the graph in the window. 

Originally, I wanted to use flask with matplotlib in order to use something more universal like a web application in order to select and display the graph. Given that I do not know any JavaScript or HTML or CSS, this proved to be extremely difficult. However, I had worked with matplotlib and tkinter before which made the revised idea much easier.
***
## Structure
```
cdc
|--data
   |--csv
      |--all of the cdc csv files
|--app.py
|--README.md
```
***
## References and resources
[csv docs](https://docs.python.org/3/library/csv.html)
[tk docs](https://docs.python.org/3/library/tk.html)
[pillow docs](https://pillow.readthedocs.io/en/stable/)
[matplotlib docs](https://matplotlib.org/stable/users/index.html)
