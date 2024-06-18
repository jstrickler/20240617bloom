import os
from datetime import date
from calendar import HTMLCalendar
import webbrowser

current_year = date.today().year

html_calendar = HTMLCalendar()  # create an HTML calendar object
formatted_year = html_calendar.formatyear(current_year)  # format one month as HTML

html_file_name = f'calendar_{current_year}.html'

with open(html_file_name, 'w') as calendar_out:
    calendar_out.write(formatted_year)  # write HTML to file
    webbrowser.open("file://" + os.path.realpath(html_file_name))  # open HTML in web browser
