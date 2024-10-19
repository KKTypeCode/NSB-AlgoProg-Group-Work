import openpyxl as xl

# TODO: IF THE LIMIT IS 0 -> Limit has not been set
wb = xl.load_workbook("Database.xlsx")
sheet1 = wb["Sheet1"]
limit = sheet1["L4"]
spending = sheet1["L5"]

def set_budget(new_limit=0):
    sheet1["L4"] = new_limit
    wb.save("Database.xlsx")
    return True

def get_limit():     #Get the budget
    return limit.value

def get_spending():
    return spending.value

print(get_limit())
print(set_budget())
print(get_limit())
