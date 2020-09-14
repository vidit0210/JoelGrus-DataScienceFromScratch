from bs4 import BeautifulSoup
import requests

URL = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')
# print(first_paragraph)
first_paragraph_text = soup.p.text
print(first_paragraph_text)

first_paragraph_words = soup.find.text.split()
print(first_paragraph_words)
