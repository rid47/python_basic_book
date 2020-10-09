from PyPDF2 import PdfFileReader
import sys

path = "D:/Ridwan/Tutorials/Real Python/Python Basic Books/code/chapter13/pandp12p.pdf"


def convertPdf2String(path):
    content = ""
    # load PDF file
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # iterate pages
    for i in range(0, pdf.getNumPages()):
        # extract the text from each page
        content += pdf.getPage(i).extractText() + " \n"
    # collapse whitespaces
    content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
    return content


# input_pdf = PdfFileReader(path)


# print(input_pdf.getNumPages())

# document_info = input_pdf.getDocumentInfo()

# title = document_info.title

# num_pages = input_pdf.getNumPages()

# print(title)


# page0_text = input_pdf.getPage(0).extractText()
# print(page0_text)

with open("Pride and Prejudice.txt", "w") as output_file:
    # output_file.write(f"{title}\n")
    # output_file.write(f"Number of pages: {num_pages}\n\n")

    # for page in input_pdf.pages:
    #     text = page.extractText()
    #     output_file.write(text)
    # page0_text = input_pdf.getPage(0).extractText().encode("utf-8")
    output_file.write(convertPdf2String(sys.argv[1]).encode("ascii", "xmlcharrefreplace"))
