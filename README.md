# Table of Contents
1. [Problem](README.md#problem)
1. [Steps to solve the problem](README.md#steps-to-submit-your-solution)
1. [Input Dataset](README.md#input-dataset)
1. [Instructions](README.md#instructions)
1. [Output](README.md#output)
1. [Tips on getting an interview](README.md#tips-on-getting-an-interview)
1. [Questions?](README.md#questions?)

# Problem

The problem at hand is to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. 

# Steps to Solve the problem
* Read the text file line by line
* Create a dictionary with drug name as a key and a list containing unique prescribers and total cost for that drug as a value 
* After the last line, sort the dictionary with descending value for total cost and ascending value for drug name if there is tie
* Write the dictionary items in an output file
