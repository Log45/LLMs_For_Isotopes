"""
This code is adapted from the tutorial at https://www.scaler.com/topics/python-html-parser/
"""

# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup


def format_html(html_file_name):
    """"""
    HTMLFile = open(f"data/html/{html_file_name}" if ".html" in html_file_name else f"data/html/{html_file_name}.html", 
                    "r", encoding="utf-8")

    # Reading the file
    index = HTMLFile.read()
    HTMLFile.close()
    # Creating a BeautifulSoup object and specifying the parser
    S = BeautifulSoup(index, 'lxml')
    S = S.prettify()

    with open(f"data/html/{html_file_name}" if ".html" in html_file_name else f"data/html/{html_file_name}.html", "w", encoding="utf-8") as f:
        f.write(S)

format_html("Production-Purification-and-Applications-of-a-Potential-Theranostic-Pair_Cobalt-55-and-Cobalt-58m-PMC.html")