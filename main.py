import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credits = ServiceAccountCredentials.from_json_keyfile_name("credits.json", scope)

client = gspread.authorize(credits)

sheet = client.open("Sheet1").sheet1

data = sheet.get_all_records()

"""
row = sheet.row_values(2)
col = sheet.col_values(2)
cell = sheet.cell(1,2).value
insertRow = ["Arild",3,10]
sheet.insert_row(insertRow,4)
sheet.delete_row(4)
sheet.update_cell(2,2,"15")
numRows = sheet.row_count
numCols = sheet.col_count
trueNumRows = len(data)
"""

