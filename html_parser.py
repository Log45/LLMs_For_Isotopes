"""
html_parser.py

This is a program to parse through research papers from mdpi.com
** THIS WILL LIKELY NOT WORK WITH PAPERS FROM ANY OTHER WEBSITE **

Author: Logan Endes 
Github: https://github.com/Log45
This code is adapted from the tutorial at https://www.scaler.com/topics/python-html-parser/ and https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-findall/#findall-by-class-and-ids
"""

# Importing BeautifulSoup class from the bs4 module
import os
from bs4 import BeautifulSoup

def extract_context(html_file_name):
    """
    Extracts paragraphs from HTML files from mdpi.com based on the class name representing paragraphs.
    """
    HTMLFile = open(f"data/html/{html_file_name}" if ".html" in html_file_name else f"data/html/{html_file_name}.html", 
                    "r", encoding="utf-8")

    # Reading the file
    index = HTMLFile.read()
    HTMLFile.close()
    # Creating a BeautifulSoup object and specifying the parser
    S = BeautifulSoup(index, 'html.parser')


    doc_title = S.title.string

    # Create a list of section names that are potentially relevant
    s = S.find_all(attrs={"data-nested": "1"})
    sections = []
    for sec in s:
        st = sec.get_text().strip()
        if "Acknowledgements" in st or "References" in st or "Funding" in st or "Conflicts" in st or "Footnotes" in st or "Author" in st or "Abbreviations" in st or "Cite" in st or "Article" in st:
            pass
        else:
            sections.append(st.replace("/n", ""))

    # Add any subsections to the sections list
    s = S.find_all(attrs={"data-nested": "2"})
    for sec in s:
        st = sec.get_text().strip()
        if "Acknowledgements" in st or "References" in st or "Funding" in st or "Conflicts" in st or "Footnotes" in st or "Author" in st or "Abbreviations" in st or "Cite" in st or "Article" in st:
            pass
        else:
            sections.append(st.replace("/n", ""))
    sections.sort()

    # Insert Abstract at index 0
    s = S.find_all(id="html-abstract-title")
    sections.insert(0, s[0].get_text().strip().replace("/n", ""))

    # Create a string with every paragraph from the paper in it.
    t = ""
    paragraphs = []
    for tag in S.find_all(class_ = 'html-p'):
        p = ""
        p += tag.get_text().strip()
        # look into .text, .item alternatives strip away formatting
        p = p.strip().replace("\n", "")
        t += p
        paragraphs.append(p)
    
    with open(f"data/html_text/{html_file_name[:-5]}.txt" if ".html" in html_file_name else f"data/html_text/{html_file_name}.txt", 
                    "w", encoding="utf-8") as f:
        f.write(t)

    return paragraphs
        

def html_to_context():
    """
    Returns:
        context: list with different paragraphs from the text file that may be able to be used as context for large language models.
        
    """
    directory = "data/html"
    context = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) and f.endswith(".html"):
            context += extract_context(filename)
    return context


def single_html_to_context(html_file_name):
    """
    Parameters:
        html_file_name: A string representation of the name of the html file.
    
    Returns:
        context: list with different paragraphs from the text file that may be able to be used as context for large language models.
    
    """
    directory = "data/html"
    if ".html" not in html_file_name:
        html_file_name = f"{html_file_name}.html"
    f = os.path.join(directory, html_file_name)
    # check if it exists
    if os.path.isfile(f) and f.endswith(".html"):
        return extract_context(html_file_name)
    print("Invalid html file: " + html_file_name)


if __name__ == "__main__":
    html_to_context()
