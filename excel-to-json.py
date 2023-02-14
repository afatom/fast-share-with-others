"""
Here is a simple Python 3 script that retrieves an Excel file and converts it to a JSON file:
This script assumes that the first column of the Excel file contains the keys, and the second column contains the values. 
If your Excel file has a different structure, you will need to modify the script accordingly.

CREDITS: chatGPT
"""

__author__ = "chatGPT"
__copyright__ = "openAI chatGPT - free copyright"

import openpyxl
import json

# Load the Excel workbook
workbook = openpyxl.load_workbook('file.xlsx')

# Select the first worksheet in the workbook
sheet = workbook.worksheets[0]

# Create an empty dictionary to store the data
data = {}

# Loop through the rows in the sheet
for row in sheet.iter_rows(values_only=True):
    # Get the values in the first and second columns
    key = row[0]
    value = row[1]
    
    # Add the key-value pair to the dictionary
    data[key] = value

# Write the dictionary to a JSON file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
