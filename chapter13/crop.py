import copy
import os


from PyPDF2 import PdfFileReader, PdfFileWriter

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter13"

input_file_path = os.path.join(path, "half_and_half.pdf")

input_pdf = PdfFileReader(input_file_path)
output_pdf = PdfFileWriter()


for page_num in range(0, input_pdf.getNumPages()):
    page_left = input_pdf.getPage(page_num)
    page_right = copy.copy(page_left)

    upper_right = page_left.mediaBox.upperRight
    print(f"upper_right: {upper_right}")
    new_coords = (upper_right[0]/2, upper_right[1])
    print(f"new coords: {new_coords}")
    page_left.mediaBox.upperRight = new_coords
    output_pdf.addPage(page_left)

    page_right.mediaBox.upperLeft = new_coords
    output_pdf.addPage(page_right)

    output_file_path = os.path.join(path, "The Little Marmaid.pdf")
    with open(output_file_path, "wb") as output_file:
        output_pdf.write(output_file)


# input_pdf = PdfFileReader(path)

# page = input_pdf.getPage(0)

# print(page.mediaBox)
# print(page.mediaBox.lowerLeft)
# print(page.mediaBox.lowerRight)
# print(page.mediaBox.upperLeft)
# print(page.mediaBox.upperRight)
