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

first_paragraph_words = soup.p.text.split()
print(first_paragraph_words)

first_paragraph_id = soup.p['id']
# Key Error if no id
first_paragraph_id2 = soup.p.get('id')
# returns None if no 'id'
all_paragraphs = soup.find_all('p')  # or just soup('p')
paragraph_with_ids = [p for p in soup('p') if p.get('id')]
print(paragraph_with_ids)

important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup(
    'p') if 'important' in p.get('class', [])]
print(important_paragraphs)
print(important_paragraphs2)
print(important_paragraphs3)

# If you
