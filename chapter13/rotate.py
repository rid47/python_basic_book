import os

from PyPDF2 import PdfFileReader, PdfFileWriter

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter13/"

input_file_path = os.path.join(path, "ugly.pdf")
input_pdf = PdfFileReader(input_file_path)
output_pdf = PdfFileWriter()

num_pages = input_pdf.getNumPages()
for n in range(0, num_pages):
    page = input_pdf.getPage(n)
    if n % 2 == 0:
        page.rotateClockwise(90)
    output_pdf.addPage(page)


output_file_path = os.path.join(path, "The confirmed Duckling.pdf")

with open(output_file_path, "wb") as output_file:
    output_pdf.write(output_file)

