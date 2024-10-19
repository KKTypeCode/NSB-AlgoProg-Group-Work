from openpyxl import load_workbook

# FOR NIXON
def add_recurring(name=None, date=None, ie=None, value=None, category=None):
    workbook = load_workbook('NSB-AlgoProg-Group-Work/Recurring.xlsx')
    workingfile = workbook.active # USE WORKINGFILE AND NOT WORKBOOK FOR WHEN EDITING CELLS
    
    # ADD NEW DATA FROM ABOVE TO NEW LINE IN EXCEL
    
    # IF STILL CANT DO, REFERENCE TO 'I&E.py'
    workbook.save('NSB-AlgoProg-Group-Work/Recurring.xlsx')