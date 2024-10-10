from openpyxl import * #type: ignore
from openpyxl.utils import get_column_letter
from pandas import * #type: ignore
"""
    REMINDER:
    - DO NOT FORGET TO INSTALL OPENPYXL IN YOUR MACHINE!
    - INSTALL IN CMD WITH: 'pip install openpyxl' / 'pip3 install openpyxl' /
            'python -m pip install openpyxl' / 'python3 -m pip install openpyxl'.
    - THE MODULE'S FILE MANIPULATOR CAN ONLY WORK WITH .xlsx FILE FORMATS (2010 ABOVE)
      AND CANNOT WORK WITH OTHER EXCEL FILE FORMATS.
    - CODE CANNOT WORK WHEN EXCEL FILE IS BEING OPENED.
"""

def income(name, value=0, category='income', delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 
 
	rowspan = 1
	colcheck = 2
	for row in range(2, rowspan+2):
		while db[str(row) + str(colcheck)] != '':
			rowspan += 1
			for col in range(2,3):
				db[str(row) + str(col)] = name
				db[str(row) + str(col+1)] = 'I'
				db[str(row) + str(col+2)] = value
				db[str(row) + str(col+3)] = category
				db[str(row) + str(col+4)] = delivered
     
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

def expense(name, value=0, category='expense', delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 
 
	rowspan = 1
	colcheck = 2
	for row in range(2, rowspan+2):
		if db[str(row) + str(colcheck)] != '':
			rowspan += 1
		else:
			for col in range(2,3):
				if db[str(row) + str(col)] != '':
					continue
				else:
					db[str(row) + str(col)] = name
					db[str(row) + str(col+1)] = 'E'
					db[str(row) + str(col+2)] = value
					db[str(row) + str(col+3)] = category
					db[str(row) + str(col+4)] = delivered 
          
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

# NOT COMPLETED // STILL HAS ERROR