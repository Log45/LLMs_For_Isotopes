"""
This code is taken from https://www.freecodecamp.org/news/extract-data-from-pdf-files-with-python/ 
"""
import pdfquery
from pdfquery import PDFQuery
import pandas
import os


def convert_to_txt(pdf_file_name:str):
    """
    Parameters:
        pdf_file_name: A string representation of the name of the pdf file.
    """
    if ".pdf" in pdf_file_name:
        pdf_file_name = pdf_file_name[:-4]

    pdf = PDFQuery(f'data/pdf/{pdf_file_name}.pdf')
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    text = [t.text for t in text_elements]

    i = 0
    for t in text:
        if t == "" or t == " " or t == "  " or t == "\n" or t == "\t":
            text.pop(i)
        i+=1

    print(text)

    ft = ""
    for t in text:
        ft += f"{t.strip()} "

    with open(f"data/txt/{pdf_file_name}.txt", "w", encoding="utf-8") as f:
        f.write(ft) 

if __name__ == "__main__":
    directory = "data/pdf"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) and f.endswith(".pdf"):
            convert_to_txt(filename)



"""
ftext = ""
for t in text:
    t.strip()
    #print(t)
    if len(t) < 50:
        text.remove(t)
    ftext += t
#print(ftext)
ftext = ftext.strip()
#print(ftext)

f = ftext.split("\n")
for x in f:
    x = x.strip()

print(f)
    """
#print(text)
"""
#read the PDF
pdf = pdfquery.PDFQuery('data/Establishing_Reliable_Cu-64_Production_Process.pdf')
pdf.load()


#convert the pdf to XML
pdf.tree.write('cu-64.xml', pretty_print = True)
print(pdf)
"""