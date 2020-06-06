import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
json_credentials = os.getenv("GOOGLE_SHEETS_CREDENTIALS_JSON")
print(json_credentials)

credentials_dict = json.loads(json_credentials)
credentials_dict["private_key"] = credentials_dict["private_key"].replace("\\\\n","\n")
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(credentials)

spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1iZpD4XQZk206__-hs6PfC2QEW7TJKTZenpKoj8mMERo/edit#gid=0")
sheet = spreadsheet.sheet1

for i in range(11):
    for j in range(11):
        sheet.update_cell(i,j,str(i*j))

"""
data = sheet.get_all_records()
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

