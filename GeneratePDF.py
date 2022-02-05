from PyPDF2 import PdfFileReader
pdf_path = 'C:\\Users\YassineT\Downloads\Documents\Conv-Payment Center For Africa-Casablanca_2.pdf'

pdf_reader = PdfFileReader(pdf_path)


with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        print(information)