import openpyxl as xl

# TODO: IF THE LIMIT IS 0 -> Limit has not been set
wb = xl.load_workbook("Database.xlsx")
sheet1 = wb["Sheet1"]
budget = sheet1["L2"]
limit = sheet1["L5"]

def set_budget(new_budget):
    sheet1["L2"] = new_budget
    wb.save("Database.xlsx")
    return True

def get_budget():     #Get the budget
    return budget.value

def set_limit(new_limit:float=0):    #set limit
    sheet1["L5"] = new_limit
    wb.save("Database.xlsx")
    return True

def get_limit():
    return limit.value

print(get_budget())
print(set_limit())
print(get_limit())
