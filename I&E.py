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

	db[get_column_letter(col) + str(row)] = name.upper()
	db[get_column_letter(col+1) + str(row)] = 'I'
	db[get_column_letter(col+2) + str(row)] = value
	db[get_column_letter(col+3) + str(row)] = category.upper()
	db[get_column_letter(col+4) + str(row)] = delivered
	
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

def expense(name, value=0, category='expense', delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 
 
	row = 2
	col = 2
	while db.cell(row=row, column=col).value != None:
		row += 1

	db[get_column_letter(col) + str(row)] = name.upper()
	db[get_column_letter(col+1) + str(row)] = 'E'
	db[get_column_letter(col+2) + str(row)] = value
	db[get_column_letter(col+3) + str(row)] = category.upper()
	db[get_column_letter(col+4) + str(row)] = delivered
          
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

def read():
    wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
    db = wb.active
    
    for row in db.iter_rows(max_col=6, min_row=2, max_row=3):
        for cell in row:
            if cell != None:
                print(cell.value, end=" ")
        print(end="\n")

# NOT DONE YET
def get_entry():
    wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
    db = wb.active
    
    for row in db.iter_cols(min_col=2, max_col=6, min_row=2):
        for cell in row:
            if cell != None:
                print(cell.value)

def change(name, ie=None, value=None, category=None, delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 

	col = 2
	entry_list = []
	
	# STILL READS BY FLOW OF B2, C2, D2 (BY COLUMN) // NEED FIX
	for col in db.iter_cols(min_row=2, max_row=2, min_col=2):
		for cell in col:
			entry_list.append(cell)
			print(cell.value)
	
	selected = input('Select entry to change: ')
	index = 0
 
	for entries in entry_list:
		index += 1
		if selected == entries:
			db[get_column_letter(2) + str(index)] = name.upper() if name != None else db[get_column_letter(2) + str(index)]
			db[get_column_letter(3) + str(index)] = ie.upper() if ie != None else db[get_column_letter(3) + str(index)]
			db[get_column_letter(4) + str(index)] = value if value != None else db[get_column_letter(4) + str(index)]
			db[get_column_letter(5) + str(index)] = category.upper() if category != None else db[get_column_letter(5) + str(index)]
			db[get_column_letter(6) + str(index)] = delivered if delivered != None else db[get_column_letter(6) + str(index)]
	else:
		print('Entry does not exist.')
  
	read()
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')
  
change('water')
