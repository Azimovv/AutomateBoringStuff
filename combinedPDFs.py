# Combines all PDFs in the current working directory into a single

import PyPDF2, os

# Get all PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all PDF files
for filename in pdfFiles:
    with open(filename, 'rb') as fileObj:
        pdfReader = PyPDF2.PdfFileReader(fileObj)
        for pageNum in range(1, pdfReader.numPages):
            fileObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(fileObj)

# Save the resulting pdf to file
with open('allminutes.pdf', 'wb') as fileObj:
    pdfWriter.write(fileObj)
