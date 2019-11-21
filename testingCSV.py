import csv, pprint

# Ideal for reading smaller files
"""with open('example.csv') as fileObj:
    exampleReader = csv.reader(fileObj)
    exampleData = list(exampleReader)

pprint.pprint(exampleData)

print(exampleData[0][0])
print(exampleData[3][1])"""

# Read via loop for larger files to avoid loading too much into memory
"""with open('example.csv') as fileObj:
    exampleReader = csv.reader(fileObj)
    for row in exampleReader:
        print(f"Row # {str(exampleReader.line_num)} {str(row)}")"""

# Writing csv files
"""with open('output.csv', 'w', newline='') as fileObj:
    outputWriter = csv.writer(fileObj)
    outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
    outputWriter.writerow(['Hello world', 'eggs', 'baccon', 'ham'])
    outputWriter.writerow([1, 2, 3.141592, 4])"""

# Delimiter and lineterminator arguments
"""with open('example.tsv', 'w', newline='') as fileObj:
    csvWriter = csv.writer(fileObj, delimiter='\t', lineterminator='\n\n')
    csvWriter.writerow(['apples', 'oranges', 'grapes'])
    csvWriter.writerow(['eggs', 'bacon', 'ham'])
    csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])"""

# DictReader and DictWriter objects
"""with open('exampleWithHeader.csv') as fileObj:
    exampleDictReader = csv.DictReader(fileObj)
    for row in exampleDictReader:
        print(row['Timestamp'], row['Fruit'], row['Quantity'])"""
# If there's no headers in the file, made up header names can be added
"""with open('example.csv') as fileObj:
    exampleDictReader = csv.DictReader(fileObj, ['time', 'name', 'amount'])
    for row in exampleDictReader:
        print(row['time'], row['name'], row['amount'])"""
with open('output.csv', 'w', newline='') as fileObj:
    outputDictWriter = csv.DictWriter(fileObj, ['Name', 'Pet', 'Phone'])
    outputDictWriter.writeheader()
    outputDictWriter.writerow({'Name': 'Alice',
                               'Pet': 'cat',
                               'Phone': '555-1234'})
    outputDictWriter.writerow({'Name': 'Bob',
                               'Phone': '555-9999'})
    outputDictWriter.writerow({'Phone': '555-5555',
                               'Name': 'Carol',
                               'Pet': 'dog'})

