from openpyxl import * #type: ignore
"""
    REMINDER:
    - DO NOT FORGET TO INSTALL OPENPYXL IN YOUR MACHINE!
    - INSTALL IN CMD WITH: 'pip install openpyxl' / 'pip3 install openpyxl' /
            'python -m pip install openpyxl' / 'python3 -m pip install openpyxl'.
    - THE MODULE'S FILE MANIPULATOR CAN ONLY WORK WITH .xlsx FILE FORMATS (2010 ABOVE)
      AND CANNOT WORK WITH OTHER EXCEL FILE FORMATS.
    - CODE CANNOT WORK WHEN EXCEL FILE IS BEING OPENED.
"""

wb = load_workbook('Database.xlsx')
db = wb.active #TO MAKE FILE EDITABLE

