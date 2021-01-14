# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:27:32 2020

@author: Andrea
"""

import csv

# opening the fact table
file1 = open("project_data/fact.csv", mode='r', encoding='utf-8-sig')
csv_sales = csv.DictReader(file1, delimiter = ",")

# opening the 3 csv output files
cpuOutputFile = 'cpu_sales.csv' 
cpucsvfile = open(cpuOutputFile, 'w', newline='')
cpuwriter = csv.writer(cpucsvfile)

gpuOutputFile = 'gpu_sales.csv' 
gpucsvfile = open(gpuOutputFile, 'w', newline='')
gpuwriter = csv.writer(gpucsvfile)

ramOutputFile = 'ram_sales.csv' 
ramcsvfile = open(ramOutputFile, 'w', newline='')
ramwriter = csv.writer(ramcsvfile)

gpu_code_key = "gpu_code"
cpu_code_key = "cpu_code"
ram_code_key = "ram_code"
id_key = "Id"

gpu_header_flag = 0
cpu_header_flag = 0
ram_header_flag = 0

for line in csv_sales:
    gpu_code = line[gpu_code_key]
    cpu_code = line[cpu_code_key]
    ram_code = line[ram_code_key]
    
    # Removing the Id column since it is a duplicate
    del line[id_key]
    
    if gpu_code != "":
        # removing the other two useless value 
        del line[cpu_code_key]
        del line[ram_code_key]
        
        # converting the id into int type
        line[gpu_code_key] = int(line[gpu_code_key].split(".")[0])
        
        # Scrivo l'header
        if gpu_header_flag == 0:
            gpuwriter.writerow(list(line.keys()))
            gpu_header_flag = 1
        
        # Scrivo la linea di valori
        gpuwriter.writerow(list(line.values()))
    elif cpu_code != "":
        del line[gpu_code_key]
        del line[ram_code_key]
        
        # converting the id into int type
        line[cpu_code_key] = int(line[cpu_code_key].split(".")[0])
        
        # Scrivo l'header 
        if cpu_header_flag == 0:
            cpuwriter.writerow(list(line.keys()))
            cpu_header_flag = 1
        
        # Scrivo la linea di valori
        cpuwriter.writerow(list(line.values()))
    elif ram_code != "":
        del line[gpu_code_key]
        del line[cpu_code_key]
        
        # converting the id into int type
        line[ram_code_key] = int(line[ram_code_key].split(".")[0])
        
        # Scrivo l'header
        if ram_header_flag == 0:
            ramwriter.writerow(list(line.keys()))
            ram_header_flag = 1
            
        ramwriter.writerow(list(line.values()))
        
        
# closing the csv output files
cpucsvfile.close()
gpucsvfile.close()
ramcsvfile.close()