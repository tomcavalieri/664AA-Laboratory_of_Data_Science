# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:23:18 2020

@author: Andrea
"""

import pyodbc
import csv

# creating a map between the database table and the file it needs to be filled with
FILE_TABLE_MAP = {
    "Vendor" : "vendor.csv",
    "Geography": "geography.csv",
    "Cpu_product": "cpu.csv",
    "Gpu_product": "gpu.csv",
    "Ram_product": "ram.csv",
    "Time": "new_elab/time_elab.csv",
    "Cpu_sales": "new_elab/cpu_sales.csv",
    "Gpu_sales": "new_elab/gpu_sales.csv",
    "Ram_sales": "new_elab/ram_sales.csv"
}

# returns a query like string from either the features or the values (returning question marks)
def create_string_from_list(arr, question_mark = 0):
    strn = ""
    
    for i, el in enumerate(arr):
        strn += el if question_mark == 0 else "?"
        
        if i != len(arr) - 1:
            strn += ", "
    
    return strn

# returns the insert into query string given the table name, the features and the values
def create_insert_query(table, features, values):
    return "INSERT INTO " + table + "(" + features + ")" + " VALUES" + "(" + values + ")"
            
# connect to data source
server = 'tcp:apa.di.unipi.it' 
database = 'Group12HWMart' 
username = 'group12' 
password = 'k3ztq' 
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString)

# per each file of the mapping
for table_key in FILE_TABLE_MAP:
    print("----- POPULATING TABLE " + table_key + "-----")
    file_name = FILE_TABLE_MAP[table_key]
    
    # opening the file
    file = open("project_data/" + file_name, mode='r', encoding='utf-8-sig')
    file_reader = csv.DictReader(file, delimiter = ",")
    
    # opening the cursor
    cursor = cnxn.cursor()

    for line in file_reader:
        # per each line of the csv it creates and execute the INSERT INTO query
        features = create_string_from_list(list(line.keys()))
        values = create_string_from_list(list(line.values()), 1)
        
        query = create_insert_query(table_key, features, values)
        print(query, tuple(line.values()))
        # Does the insert and then commit the transaction
        cursor.execute(query, tuple(line.values()))
        cnxn.commit()
    
    # closing the cursor and the file
    cursor.close()
    file.close()
    
# closing the DB connection
cnxn.close()