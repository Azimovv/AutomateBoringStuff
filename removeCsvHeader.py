# Removes headers from all CSV files in working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # skip non-csv files
    print(f'Removing header from {csvFilename}...')

    # Read the CSV file in (skipping first row)
    csvRows = []
    with open(csvFilename) as fileObj:
        readerObj = csv.reader(fileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue  # skip first row
            csvRows.append(row)

    # Write out the CSV file
    with open(os.path.join('headerRemoved', csvFilename),
              'w', newline='') as fileObj:
        csvWriter = csv.writer(fileObj)
        for row in csvRows:
            csvWriter.writerow(row)