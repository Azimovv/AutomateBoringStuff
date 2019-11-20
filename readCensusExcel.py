# Tabulates population and number of census tracts for each county

import openpyxl, pprint
print("Opening workbook...")
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, increment by 1
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

print("Writing results...")
with open('census2010.py', 'w') as fileObj:
    fileObj.write('allData = ' + pprint.pformat(countyData))

print("Done.")