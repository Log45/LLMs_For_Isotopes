"""
This code is taken from https://www.freecodecamp.org/news/extract-data-from-pdf-files-with-python/ 
"""
import pdfquery
from pdfquery import PDFQuery
import pandas

s = "To assess the quality and quantity of the produced 64Cu, we made 64Cu-DOTA-rituximab"
print(len(s))

pdf = PDFQuery('data/Establishing_Reliable_Cu-64_Production_Process.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)
i = 0
for t in text:
    if t == "" or t == " " or t == "  " or t == "\n" or t == "\t":
        text.pop(i)
    i+=1

print(text)

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