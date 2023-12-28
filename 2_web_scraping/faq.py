import requests
from bs4 import BeautifulSoup
import time 

#FAQ zu Prüfungsangelegenheiten der Bachelorstudiengänge AIN, GIB und WIN 
#url = "https://www.htwg-konstanz.de/hochschule/fakultaeten/informatik/studium/pruefungen-thesis/faq"

#FAQ zu Prüfungen der HTWG
url = "https://www.htwg-konstanz.de/studium/faq/pruefungen"

# Send an HTTP request to the URL and get the page content
response = requests.get(url)
html = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Open a text file to save the data
with open("faq_data2.txt", "w", encoding="utf-8") as file:

    # Find all elements with class "title icon"
    title_icon_elements = soup.find_all(class_="title icon")

    for idx,element in enumerate(title_icon_elements):
        # Save the text inside the "title icon" element
        title_text = element.get_text(strip=True)

        answers = soup.select('.frame.default.frame-default.frame-type-text.frame-layout-0.frame-space-before-medium.frame-space-after-medium, .frame.default.frame-default.frame-type-text.frame-layout-0')#accordion_element = soup.find_all(class_='frame default frame-default frame-type-text frame-layout-0')
        file.write(f"Frage: {title_text}\n")

        if answers:                      
            for idx2,paragraph in enumerate(answers):
                paragraph_text = paragraph.get_text(strip=False)
                if idx == idx2:
                    file.write(f"Antwort: {paragraph_text}\n")
                    file.write("\n")
                    break
                
                
print("Data saved to 'faq_data.txt'")
time.sleep(1)

