"""
This code is adapted from the tutorial at https://www.scaler.com/topics/python-html-parser/
"""

# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
from html.parser import HTMLParser

def html_to_context(html_file_name):
    """"""
    HTMLFile = open(f"data/html/{html_file_name}" if ".html" in html_file_name else f"data/html/{html_file_name}.html", 
                    "r", encoding="utf-8")

    # Reading the file
    index = HTMLFile.read()
    HTMLFile.close()
    # Creating a BeautifulSoup object and specifying the parser
    S = BeautifulSoup(index, 'html.parser')


    doc_title = S.title.string
    print(doc_title)
    
    # Create a list of section names that are potentially relevant
    s = S.find_all(attrs={"data-nested": "1"})#, class_ = 'html-body')
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
    print(sections)



    # Create a string with every paragraph from the paper in it.
    t = ""
    paragraphs = []
    for tag in S.find_all(class_ = 'html-p'):
        #print(tag)
        #print(tag.get("html-p"))
        t += tag.get_text().strip()
        # look into .text, .item alternatives strip away formatting
        t = t.strip().replace("\n", "")
        paragraphs.append(t)
    print(paragraphs)
    
    #if not f"data/html_text/{html_file_name[:-5]}.txt" if ".html" in html_file_name else f"data/html_text/{html_file_name}.txt":
    with open(f"data/html_text/{html_file_name[:-5]}.txt" if ".html" in html_file_name else f"data/html_text/{html_file_name}.txt", 
                    "w", encoding="utf-8") as f:
        f.write(t)
        

if __name__ == "__main__":
    #format_html("Production_Purification_and_Applications_of_a_Potential_Theranostic_Pair_Cobalt-55_and_Cobalt-58m")
    html_to_context("641")
    html_to_context("Production_Purification_and_Applications_of_a_Potential_Theranostic_Pair_Cobalt-55_and_Cobalt-58m")
