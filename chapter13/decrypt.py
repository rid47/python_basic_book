import os

from PyPDF2 import PdfFileReader

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter13"

input_file_path = os.path.join(path, "New Suit Enc.pdf")
input_pdf = PdfFileReader(input_file_path)

# input_pdf.decrypt("124")

for page in input_pdf.pages:
    text = page.extractText()
    print(text)
