from bs4 import BeautifulSoup

def extract_text_by_class(html_file, class_name):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(class_=class_name)

    extracted_text = []
    for element in elements:
        extracted_text.append(element.get_text().strip())

    return extracted_text

if __name__ == "__main__":
    # Replace 'your_html_file.html' with the path to your HTML file
    html_file_path = 'data\html\Production_Purification_and_Applications_of_a_Potential_Theranostic_Pair_Cobalt-55_and_Cobalt-58m.html'
    target_class_name = 'html-p'  # Replace 'your-class-name' with the desired class name

    extracted_text_list = extract_text_by_class(html_file_path, target_class_name)

    # Print the extracted text
    for text in extracted_text_list:
        print(text)