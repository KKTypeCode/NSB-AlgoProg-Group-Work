from openpyxl import * #type: ignore
from openpyxl.utils import get_column_letter

"""
    REMINDER:
    - DO NOT FORGET TO INSTALL OPENPYXL IN YOUR MACHINE!
    - INSTALL IN CMD WITH: 'pip install openpyxl' / 'pip3 install openpyxl' /
            'python -m pip install openpyxl' / 'python3 -m pip install openpyxl'.
    - THE MODULE'S FILE MANIPULATOR CAN ONLY WORK WITH .xlsx FILE FORMATS (2010 ABOVE)
      AND CANNOT WORK WITH OTHER EXCEL FILE FORMATS.
    - CODE CANNOT WORK WHEN EXCEL FILE IS BEING OPENED.
"""

# ADD NEW ENTRY FOR INCOME & EXPENSE

def income(name, value=0, category='income', delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 
 
	row = 2
	col = 2
	while db.cell(row=row, column=col).value != None:
		row += 1

	db[get_column_letter(col) + str(row)] = name
	db[get_column_letter(col+1) + str(row)] = 'I'
	db[get_column_letter(col+2) + str(row)] = value
	db[get_column_letter(col+3) + str(row)] = category
	db[get_column_letter(col+4) + str(row)] = delivered
	
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

def expense(name, value=0, category='expense', delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 
 
	row = 2
	col = 2
	while db.cell(row=row, column=col).value != None:
		row += 1

	db[get_column_letter(col) + str(row)] = name
	db[get_column_letter(col+1) + str(row)] = 'E'
	db[get_column_letter(col+2) + str(row)] = value
	db[get_column_letter(col+3) + str(row)] = category
	db[get_column_letter(col+4) + str(row)] = delivered
          
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

