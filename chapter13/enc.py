import os

from PyPDF2 import PdfFileReader, PdfFileWriter

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter13"


input_file_path = os.path.join(path, "New Suit.pdf")
input_pdf = PdfFileReader(input_file_path)
output_pdf = PdfFileWriter()

for page in input_pdf.pages:
    output_pdf.addPage(page)

output_pdf.encrypt("124")

output_file_path = os.path.join(path, "New Suit Enc.pdf")
with open(output_file_path, "wb") as f:
    output_pdf.write(f)



