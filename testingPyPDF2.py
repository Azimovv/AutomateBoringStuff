# Testing out PyPDF2

import PyPDF2


with open('meetingminutes.pdf', 'rb') as fileObj:
    # Reading a file
    pdfReader = PyPDF2.PdfFileReader(fileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())

with open('encrypted.pdf', 'rb') as fileObj:
    # Opening an encrypted file
    pdfReader = PyPDF2.PdfFileReader(fileObj)
    print(pdfReader.isEncrypted)
    pdfReader.decrypt('rosebud')
    pageObj = pdfReader.getPage(0)

with open('meetingminutes.pdf', 'rb') as fileObj1, \
        open('meetingminutes2.pdf', 'rb') as fileObj2:
    # Writing files (copying from one pdf to another)
    pdf1Reader = PyPDF2.PdfFileReader(fileObj1)
    pdf2Reader = PyPDF2.PdfFileReader(fileObj2)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    pdfOutput = open('combinedminutes.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()

with open('meetingminutes.pdf', 'rb') as fileObj:
    # Adding a watermark using the merge ability
    pdfReader = PyPDF2.PdfFileReader(fileObj)
    minutesFirstPage = pdfReader.getPage(0)
    pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
    minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(minutesFirstPage)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    resultPdfFile = open('watermarkedCover.pdf', 'wb')
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()

with open('meetingminutes.pdf', 'rb') as fileObj:
    # Encrypting a pdf
    pdfReader = PyPDF2.PdfFileReader(fileObj)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt('swordfish')
    resultPdf = open('encryptedminutes.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()