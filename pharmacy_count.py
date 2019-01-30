# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:19:36 2019

@author: Asus
"""

import sys
# filename
#input_file = str(sys.argv[1])
input_file = r'C:\Users\Asus\Documents\GitHub\pharmacy_count\itcont.txt'
# reading the rest of the file
data = []
drugs = {}
with open(input_file, 'r') as file:
    headers = next(file).strip('\n').split(',')
    # variable indices
    prescriber_id = headers.index('id')
    drug_name = headers.index('drug_name')
    drug_cost = headers.index('drug_cost')
    # reading the data
    for line in file:
        line = line.strip('\n').split(',')
        # line = [line[prescriber_id], line[drug_name], line[drug_cost]]
        #prescriber_id = int(line[prescriber_id])
        if line[drug_name] in drugs:
            if line[prescriber_id] not in drugs[line[drug_name]][0]:
                drugs[line[drug_name]][0].append(line[prescriber_id])
            drugs[line[drug_name]][1] += int(line[drug_cost])                
        else:
            drugs[line[drug_name]] = [[line[prescriber_id]], int(line[drug_cost])]
      
output_data = sorted(drugs.items(), key=lambda x: (-x[1][1], x[0]))    
output_file = r'C:\Users\Asus\Documents\GitHub\pharmacy_count\top_cost_drug.txt'
#output_file = str(sys.argv[2])
with open(output_file,"w") as file1:
    output = ["drug_name,num_prescriber,total_cost\n"]
    output += [output_line[0] + ',' + str(len(output_line[1][0])) + ',' + 
               str(output_line[1][1]) + '\n' for output_line in output_data]     
    file1.writelines(output)