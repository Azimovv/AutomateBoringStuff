import win32com.client
import docx

# Need Microsoft Word installed on computer for this to work
wordFilename = 'document_name.docx'
pdfFilename = 'pdf_name.pdf'

doc = docx.Document()
# Create Word Document here
""" ~~~~~~~~~~~~~~~~~~~~~~~~~ """
doc.save(wordFilename)

wdFormatPDF = 17  # Word's code for PDFs
wordObj = win32com.client.Dispatch('Word.Application')

docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.close()
wordObj.Quit()