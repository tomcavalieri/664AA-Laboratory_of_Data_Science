# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:50:37 2020

@author: Andrea
"""

import csv
import datetime

def get_quarter(month):
    if month <= 3:
        return 1
    elif month > 3 and month <= 6:
        return 2
    elif month > 6 and month <= 9:
        return 3
    else:
        return 4

# opening the old time.csv
time_csv = open("project_data/time.csv", mode='r', encoding='utf-8-sig')
time_table = csv.DictReader(time_csv, delimiter = ",")

# getting the features name
headers = time_table.fieldnames

# opening the new csv file
timeOutputFile = 'time_elab.csv'
timecsvfile = open(timeOutputFile, 'w', newline='')
timewriter = csv.writer(timecsvfile)

day_of_week_key = "day_of_week"
quarter_key = "quarter"

# adding the new columns to the header list
headers.append(day_of_week_key)
headers.append(quarter_key)

# writing the new header
timewriter.writerow(headers)

for line in time_table:
    day = int(line["day"])
    month = int(line["month"])
    year = int(line["year"])
    
    line[day_of_week_key] = datetime.datetime(year, month, day).strftime("%A")
    line[quarter_key] = "Q" + str(get_quarter(month))
    
    line_values = list(line.values())
    timewriter.writerow(line_values)
    
time_csv.close()
timecsvfile.close()