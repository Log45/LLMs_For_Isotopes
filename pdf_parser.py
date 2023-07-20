"""
pdf_parser.py is a program that uses the pdfquery library to take pdfs and convert them into a list of paragraphs that may be able to be used as context in prompts for large language models.
Author: Logan Endes https://github.com/Log45
Code for accessing pdfs with PDFQuery adapted from https://www.freecodecamp.org/news/extract-data-from-pdf-files-with-python/ 
"""
import pdfquery
from pdfquery import PDFQuery
import os

def convert_to_txt(pdf_file_name:str):
    """
    Parameters:
        pdf_file_name: A string representation of the name of the pdf file.
    """
    if ".pdf" in pdf_file_name:
        pdf_file_name = pdf_file_name[:-4]

    if os.path.isfile(f"data/txt/{pdf_file_name}.txt"):
        pass
    else:
        pdf = PDFQuery(f'data/pdf/{pdf_file_name}.pdf')
        pdf.load()

        # Use CSS-like selectors to locate the elements
        text_elements = pdf.pq('LTTextLineHorizontal')

        # Extract the text from the elements
        text = [t.text for t in text_elements]

        ft = ""
        for t in text:
            ft += f"{t.strip()} "

        with open(f"data/txt/{pdf_file_name}.txt", "w", encoding="utf-8") as f:
            f.write(ft) 


def extract_context(txt_file_name):
    """
    Parameters: 
        txt_file_name: A string representation fo the name of the txt file (converted from pdf).
    
    Returns:
        context: list with different paragraphs from the text file that may be able to be used as context for large language models.
    """
    if ".txt" not in txt_file_name:
        txt_file_name = f"{txt_file_name}.txt"
    
    s = ""
    with open(f"data/txt/{txt_file_name}", "r", encoding="utf-8") as f:
        for line in f:
            s += f"{line.strip()} "
    
    context = s.split("  ")
    
    i = 0
    remove = []
    # print(len(context))
    
    for p in context:
        if len(p) < 5:
            remove.append(i)
        i+=1
    x=0
    for i in remove:
        context.pop(i-x)
        x+=1
    # print(len(context))
    
    return context


def pdf_to_context():
    """
    Returns:
        context: list with different paragraphs from the text file that may be able to be used as context for large language models.
        
    Note: While this program does split pdfs into different paragraphs, it is not guaranteed that the produced paragraphs are all usable, and there 
    are still a good number of paragraphs that are simply acknowledgements or unusable blocks of text from the pdfs. 
    """
    directory = "data/pdf"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) and f.endswith(".pdf"):
            convert_to_txt(filename)

    directory = "data/txt"
    context = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # check if it is a file and run the context extractor
        if os.path.isfile(f) and f.endswith(".txt"):
            context += (extract_context(filename))
    # for _ in context:
        # print(_, end="\t \end/ \n\n")
    return context

if __name__ == "__main__":
    pdf_to_context()
