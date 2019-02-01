# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:19:36 2019

@author: Asus
"""
import sys
# functions to use
def infer_data_type(input_data):
    with open(input_data) as file:
        next(file)
        test_number = next(file).strip('\n').split(',')[-1]
        try:
            int(test_number)
        except ValueError:
            return float
    return int
# filename
input_file = str(sys.argv[1])
dictionary = {}
number_type = infer_data_type(input_data=input_file)
with open(input_file) as file:
    headers = next(file).strip('\n').split(',')
    # variable indices
    prescriber_id_idx = headers.index('id')
    drug_name_idx = -2
    drug_cost_idx = -1
    prev_prescriber = None
    for line in file:
        # we strip \n and put them in a list
        obs_list = line.strip('\n').split(',')
        # some testing showed that there are double quotes so we strip them
        sample_drug = obs_list[drug_name_idx].strip('"')
        # if same prescriber id, we do not need to get the names
        if obs_list[0] != prev_prescriber:
            name = (obs_list[1] + ' ' + obs_list[-3]).split(' ')
            name = name[0] + ' ' + name[-1]
        # creating a variable to refer to its cost
        cost = number_type(obs_list[drug_cost_idx])
        # if drug is new occurrence then we have it as a new key 
        if sample_drug in dictionary.keys():
            dictionary[sample_drug][1] += cost
            dictionary[sample_drug][0].add(name)
        else:
            dictionary[sample_drug] = [{name}, cost]
        prev_prescriber = obs_list[0]    

# we sort our dictionary according to decreasing cost       
output_data = sorted(dictionary.items(), key=lambda x: (-x[1][1], x[0]))
# outputting to a file     
file1 = open(str(sys.argv[2]), "w")
output = ["drug_name,num_prescriber,total_cost\n"]
output += [output_line[0] + "," + str(len(output_line[1][0])) + "," + 
           str(output_line[1][1]) + "\n" for output_line in output_data]     
file1.writelines(output)
file1.close()