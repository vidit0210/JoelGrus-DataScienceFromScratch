import re
from bs4 import BeautifulSoup
import requests
URL = "https://www.house.gov/representatives"

text = requests.get(URL).text
soup = BeautifulSoup(text, "html5lib")

all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
print(len(all_urls))

# Must start with http:// or https://
# Must end with .house.gov or .house.gov/
regex = r"^https?://.*\.house\.gov/?$"

# Let's write some tests!
assert re.match(regex, "http://joel.house.gov")
assert re.match(regex, "https://joel.house.gov")
assert re.match(regex, "http://joel.house.gov/")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, "joel.house.gov")
assert not re.match(regex, "http://joel.house.com")
assert not re.match(regex, "https://joel.house.gov/biography")

good_urls = [url for url in all_urls if re.match(regex, url)]
print(len(good_urls))
good_urls = list(set(good_urls))
print(len(good_urls))
