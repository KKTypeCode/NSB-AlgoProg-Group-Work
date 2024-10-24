import openpyxl as xl

# TODO: IF THE LIMIT IS 0 -> Limit has not been set
wb = xl.load_workbook("NSB-AlgoProg-Group-Work/Database.xlsx")
sheet1 = wb.active
limit = sheet1["L5"].value
spending = sheet1["L6"].value

def set_budget(new_limit=0):
    sheet1["L5"].value = new_limit
    wb.save("Database.xlsx")
    wb.close

def get_limit():
    return limit

def get_spending():
    return spending
