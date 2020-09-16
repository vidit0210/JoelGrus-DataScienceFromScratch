from house_url in good_urls:
from typing import Dict, Set
html = requests.get('https://jayapal.house.gov').text
soup = BeautifulSoup(html, 'html5lib')

links = {a['href'] for a in soup('a') if 'press releases' in text.lower()}
print(links)

press_releases = Dict[str, Set[str]] = {}

html = requests.get(house_url).text
soup = BeautifulSoup(html, 'html5lib')
pr_links = {a['href'] a for a in soup if 'press releases' a.text.lower()}
print(f"{house_url}:{pr_links}")
press_releases[house_url] = pr_links


def paragraph_mentions(text: str, keyword: str):
