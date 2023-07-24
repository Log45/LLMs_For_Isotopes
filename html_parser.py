"""
This code is adapted from the tutorial at https://www.scaler.com/topics/python-html-parser/
"""

# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
from html.parser import HTMLParser

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


def html_to_context(html_file_name):
    """"""
    HTMLFile = open(f"data/html/{html_file_name}" if ".html" in html_file_name else f"data/html/{html_file_name}.html", 
                    "r", encoding="utf-8")

    # Reading the file
    index = HTMLFile.read()
    HTMLFile.close()
    # Creating a BeautifulSoup object and specifying the parser
    S = BeautifulSoup(index, 'html.parser')
    # Look for these classes:
    # html-p
    # title hypothesis_container
    # h2 for section headers
    # h4 for subsection headers
    # relevant ids all contain 'secx-diagnostics'
    

    # look for "p p-first"
    # look for "p p-first-last"
    # look for "p p-last"
    # look for h3 id="secx... for section headers

    

    doc_title = S.title.string
    t = ""
    #print(body)
    #print(S.find_all(class_ = 'p-first'))
    
    
    # Create a list of section names that are potentially relevant
    s = S.find_all(class_ = 'head no_bottom_margin ui-helper-clearfix')
    sections = []
    for sec in s:
        st = sec.text.strip()
        if "Acknowledgements" in st or "References" in st or "Funding" in st or "Conflicts" in st or "Footnotes" in st or "Author" in st or "Abbreviations" in st:
            pass
        else:
            sections.append(st)
    print(sections)

    for tag in S.find_all('section'):
        #print(tag)
        #print(tag.get("html-p"))
        t += tag.text
        # look into .text, .item alternatives strip away formatting
        t = t.strip()
        # print(f'{tag.name}: {tag.text}')
    #print(t)
    
    #if not f"data/html_text/{html_file_name[:-5]}.txt" if ".html" in html_file_name else f"data/html/{html_file_name}.txt":
    with open(f"data/html_text/{html_file_name[:-5]}.txt" if ".html" in html_file_name else f"data/html/{html_file_name}.txt", 
                    "w", encoding="utf-8") as f:
        f.write(t)
        

if __name__ == "__main__":
    format_html("Production-Purification-and-Applications-of-a-Potential-Theranostic-Pair_Cobalt-55-and-Cobalt-58m-PMC.html")
    #html_to_context("Production-Purification-and-Applications-of-a-Potential-Theranostic-Pair_Cobalt-55-and-Cobalt-58m-PMC.html")
