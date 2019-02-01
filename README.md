# Table of Contents
1. [Problem](README.md#problem)
1. [Steps to solve the problem](README.md#steps-to-solve-the-problem)
1. [Run Instructions](README.md#run-instructions)
1. [Notes](README.md#notes)

# Problem

The problem at hand is to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. 

# Steps to solve the problem
* Read the text file line by line
* Create a dictionary with drug name as a key and a list containing unique prescribers and total cost for that drug as a value 
* After the last line, sort the dictionary with descending value for total cost and ascending value for drug name if there is tie
* Write the dictionary items in an output file

# Run Instructions
Using the command line on a Linux machine, you run the same way as in run.sh file except for three arguments you have to specify the location of the data file along with its name and locations for output files along with the names you give to the files.

# Notes

