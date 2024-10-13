from openpyxl import * #type: ignore
from openpyxl.utils import get_column_letter
import datetime as dt

"""
    REMINDER:
    - DO NOT FORGET TO INSTALL OPENPYXL IN YOUR MACHINE!
    - INSTALL IN CMD WITH: 'pip install openpyxl' / 'pip3 install openpyxl' /
            'python -m pip install openpyxl' / 'python3 -m pip install openpyxl'.
    - THE MODULE'S FILE MANIPULATOR CAN ONLY WORK WITH .xlsx FILE FORMATS (2010 ABOVE)
      AND CANNOT WORK WITH OTHER EXCEL FILE FORMATS.
    - CODE CANNOT WORK WHEN EXCEL FILE IS BEING OPENED.
"""

# GENERATE A SPECIAL ID KEY TO ALLOW DIFFERENCE BETWEEN ENTRIES

def gen_id_key():
    with open('NSB-AlgoProg-Group-Work/Set_Const.txt', 'r') as file:
        current_value = int(file.readline().strip().split('ID ')[-1])
        new_value = current_value + 1
        id_key = f"{current_value:06d}"
    
    with open('NSB-AlgoProg-Group-Work/Set_Const.txt', 'w') as file:
        file.seek(0)
        file.write(f"ID {new_value:06d}")
        
    return id_key

# GENERATE CURRENT DATE AND TIME
    
def date():
    current_date = dt.datetime.now().date()
    return current_date.strftime("%Y-%m-%d")

def time():
    timezone = dt.timezone(dt.timedelta(hours=7))
    current_time = dt.datetime.now(timezone).time()
    return current_time.strftime("%H:%M:%S")

# ADD INCOME AND EXPENSE ENTRIES TO THE DATABASE
    
def income(name, value=0, category='income', delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 
 
	row = 2
	col = 2
	while db.cell(row=row, column=col).value != None:
		row += 1

	db[get_column_letter(col) + str(row)] = name.upper()
	db[get_column_letter(col+1) + str(row)] = date()
	db[get_column_letter(col+2) + str(row)] = 'I'
	db[get_column_letter(col+3) + str(row)] = value
	db[get_column_letter(col+4) + str(row)] = category.upper()
	db[get_column_letter(col+5) + str(row)] = delivered
	db[get_column_letter(col+6) + str(row)] = gen_id_key()
	db[get_column_letter(col+7) + str(row)] = f"{date()} / {time()}"

	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

def expense(name, value=0, category='expense', delivered=False):
	wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
	db = wb.active 
 
	row = 2
	col = 2
	while db.cell(row=row, column=col).value != None:
		row += 1

	db[get_column_letter(col) + str(row)] = name.upper()
	db[get_column_letter(col+1) + str(row)] = date()
	db[get_column_letter(col+2) + str(row)] = 'E'
	db[get_column_letter(col+3) + str(row)] = value
	db[get_column_letter(col+4) + str(row)] = category.upper()
	db[get_column_letter(col+5) + str(row)] = delivered
	db[get_column_letter(col+6) + str(row)] = gen_id_key()
	db[get_column_letter(col+7) + str(row)] = f"{date()} / {time()}"
    
	wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

# MODIFY ENTRIES IN THE DATABASE

def read():
    wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
    db = wb.active
    
    for row in db.iter_rows(max_col=8, min_row=2, max_row=db.max_row):
        for cell in row:
            if cell.value != None:
                print(cell.value, end=" ")
        print('', end="\n")

def change(name=None, ie=None, value=None, category=None, delivered=None):
    wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
    db = wb.active

    entry_list = []
    
    print("Available entries:")
    for column in db.iter_cols(min_row=2, min_col=2, max_col=2):
        for cell in column:
            if cell.value != None:
                entry_list.append(cell.value)

    selected = str(input('Select entry to change: ')).strip().upper()

    if selected not in entry_list:
        print('Entry does not exist.')
    else:
        index = entry_list.index(selected) + 2 
        db[get_column_letter(2) + str(index)] = name if name != None else db[get_column_letter(2) + str(index)].value
        db[get_column_letter(3) + str(index)] = ie.upper() if ie != None else db[get_column_letter(3) + str(index)].value
        db[get_column_letter(4) + str(index)] = value if value != None else db[get_column_letter(4) + str(index)].value
        db[get_column_letter(5) + str(index)] = category.upper() if category != None else db[get_column_letter(5) + str(index)].value
        db[get_column_letter(6) + str(index)] = delivered if delivered != None else db[get_column_letter(6) + str(index)].value
        
    read()
    wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')
    
def delete():
    wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
    db = wb.active

    entry_list = []
    
    print("Available entries:")
    for column in db.iter_cols(min_row=2, min_col=2, max_col=2):
        for cell in column:
            if cell.value != None:
                entry_list.append(cell.value)

    selected = str(input('Select entry to delete: ')).strip().upper()

    if selected not in entry_list:
        print('Entry does not exist.')
    else:
        index = entry_list.index(selected) + 2 
        db[get_column_letter(2) + str(index)] = None
        db[get_column_letter(3) + str(index)] = None
        db[get_column_letter(4) + str(index)] = None
        db[get_column_letter(5) + str(index)] = None
        db[get_column_letter(6) + str(index)] = None
        db[get_column_letter(7) + str(index)] = None
        
    read()
    wb.save('NSB-AlgoProg-Group-Work/Database.xlsx')

# TESTING
income('Commission', 1000, delivered=True)

# NOTE:
# CODE HAS NOT BEEN FULLY TESTED YET // STILL NEED MORE TESTING
# ADDITION OF BALANCE FUNCTIONALITY IS REQUIRED