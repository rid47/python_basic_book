import os

from PyPDF2 import PdfFileReader, PdfFileWriter

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter13"


input_file_path = os.path.join(path, "The Emperor.pdf")
input_pdf = PdfFileReader(input_file_path)
output_pdf = PdfFileWriter()

watermark_file_path = os.path.join(path, "top_secret.pdf")
watrermark_pdf = PdfFileReader(watermark_file_path)
watermark_page = watrermark_pdf.getPage(0)

for page in input_pdf.pages:
    page.mergePage(watermark_page)
    output_pdf.addPage(page)

output_file_path = os.path.join(path, "New Suit.pdf")
with open(output_file_path, "wb") as output_file:
    output_pdf.write(output_file)
