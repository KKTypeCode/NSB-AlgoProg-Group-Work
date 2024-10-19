from openpyxl import Workbook, load_workbook
import os

# Function to append data to Excel using openpyxl
def append_data_to_excel(data, file_path, sheet_name="Sheet1"):
    # Check if the file exists
    if os.path.exists(file_path):
        # Load existing workbook
        workbook = load_workbook(file_path)
        worksheet = workbook[sheet_name] if sheet_name in workbook.sheetnames else workbook.active
    else:
        # Create a new workbook and worksheet
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = sheet_name
        # Write header if creating a new file
        worksheet.append(['Date', 'Value'])

    # Append new data
    worksheet.append(data)

    # Save the workbook
    workbook.save(file_path)

# Example recurring data
new_data = ['2024-10-19', 100]

# Append the new data to the Excel file
file_path = 'recurring_data.xlsx'
append_data_to_excel(new_data, file_path)