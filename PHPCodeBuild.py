#https://www.geeksforgeeks.org/reading-excel-file-using-python/

# Reading an excel file using Python 
import xlrd
from pathlib import Path
#import array 
  
# Give the location of the file for variable reading
loc = Path("{FILEPATHofXLSXFILE}")
# To open Workbook  
#Method 1
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

#https://linuxhandbook.com/python-write-list-file/
#opening up file
textFile = open('xlsToPHPOutput.txt', 'w')

for i in range(1, sheet.nrows):
    #check to see if value is empty in one cell, apply appropriate code if true
    if sheet.cell_value(i,1) == "":
        print("\n//variable not used in database" , file=textFile)
        print("$" + sheet.cell_value(i,0) + " = $_POST[\'" + sheet.cell_value(i,0) + "\'];\n" , file=textFile)
    elif sheet.cell_value(i,0) == "":
        print("\n//variable POSSIBLY not used in database" , file=textFile)
        print("$" + sheet.cell_value(i,1) + " = $_POST[\'" + sheet.cell_value(i,1) + "\'];\n" , file=textFile)
    else:
        print("$" + sheet.cell_value(i,1) + " = $_POST[\'" + sheet.cell_value(i,0) + "\'];" , file=textFile)
        #this is to create get-functions for each of the variables
        #print("function get"+sheet.cell_value(i,1)+"(){", file=textFile)
        #print("    return $" + sheet.cell_value(i,1)+";", file=textFile)
        #print("}", file=textFile)
    