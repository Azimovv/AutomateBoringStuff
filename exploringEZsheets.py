# Testing out various commands and utilities of the EZsheets module

import ezsheets

ss = ezsheets.Spreadsheet('11gn7L4eP2jhKuzG1-fcGqGZ1BC0KKHbB6emQ_G9zAO4')
print(ss)
print(ss.title)

ss = ezsheets.createSpreadsheet('Testing EZsheets')
print(ss.title)

ss = ezsheets.upload('censuspopdata.xlsx')
print(ss.title)

print(ezsheets.listSpreadsheets())

ss.title = "Top r/Science posts"
print(ss.spreadsheetId)     # get spreadsheet ID
print(ss.url)               # get spreadsheet url
print(ss.sheetTitles)       # get titles of all sheet objects
print(ss.sheets)            # get sheet objects in order
print(ss[0])                # get first sheet object

print(ss.title)
ss.downloadAsCSV()        # Download spreadsheet as CSV file
ss.downloadAsExcel()      # Download spreadsheet as Excel file
ss.downloadAsHTML()       # Download spreadsheet as ZIP of HTML files
ss.downloadAsODS()        # Download spreadsheet as OpenOffice file
ss.downloadAsPDF()        # Download spreadsheet as PDF file
ss.downloadAsTSV()        # Download spreadsheet as TSV file

ss = ezsheets.createSpreadsheet('My spreadsheet')
sheet = ss[0]
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'
sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'Robocop'

ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]
sheet.getRow(1)
sheet.getRow(2)
columnOne = sheet.getColumn(1)
sheet.getColumn(1)
sheet.getColumn('A')
sheet.getRow(3)
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
sheet.getRow(3)
for i, value in enumerate(columnOne):
    # Make python list contain uppercase strings
    columnOne[i] = value.upper()

sheet.updateColumn(1, columnOne)  # Update entire column in one

rows = sheet.getRows()  # get every row in spreadsheet
print(rows[0])
print(rows[1])
rows[1][0] = 'PUMPKIN'  # Change produce name
print(rows[1])
print(rows[10])
rows[10][2] = '400'  # Change pounds sold
rows[10][3] = '904'  # Change the total
print(rows[10])
sheet.updateRows(rows)  # Update online spreadsheet with changes

print(sheet.rowCount)
print(sheet.columnCount)
sheet.columnCount = 4
print(sheet.columnCount)

ss1 = ezsheets.createSpreadsheet('First spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second spreadsheet')
ss1[0].copyTo(ss2)