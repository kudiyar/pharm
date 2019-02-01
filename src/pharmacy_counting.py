# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:19:36 2019

@author: Asus
"""

import sys
# filename
input_file = str(sys.argv[1])
dictionary = {}
def data_type_identify(input_data):
    with open(input_data) as file:
        next(file)
        test_number = next(file).strip('\n').split(',')[-1]
        try:
            int(test_number)
        except ValueError:
            return float
    return int

number_type = data_type_identify(input_data=input_file)
with open(input_file) as file:
    headers = next(file).strip('\n').split(',')
    # variable indices
    prescriber_id_idx = headers.index('id')
    drug_name_idx = -2
    drug_cost_idx = -1
    for line in file:
        line = line.strip('\n').split(',')
        sample_drug = line[drug_name_idx].strip('"')
        name = (line[1] + ' ' + line[-3]).split(' ')
        name = name[0] + ' ' + name[-1]
        cost = number_type(line[drug_cost_idx])
        if sample_drug in dictionary.keys():
            dictionary[sample_drug][1] += cost
            dictionary[sample_drug][0].add(name)
        else:
            dictionary[sample_drug] = [{name}, cost]

output_data = sorted(dictionary.items(), key=lambda x: (-x[1][1], x[0]))    
file1 = open(str(sys.argv[2]), "w")
output = ["drug_name,num_prescriber,total_cost\n"]
output += [output_line[0] + "," + str(len(output_line[1][0])) + "," + 
           str(output_line[1][1]) + "\n" for output_line in output_data]     
file1.writelines(output)
file1.close()