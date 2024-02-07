import requests
from bs4 import BeautifulSoup
import time

base_url = "https://visitseattle.org/events/page/{page_number}/?frm=events&event_type&s"

all_links = []

for page_number in range(1, 42):
    time.sleep(5)
    url = base_url.format(page_number=page_number)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for a_tag in soup.select('div.search-result-preview > div > h3 > a'):
            if 'href' in a_tag.attrs:
                all_links.append(a_tag['href'])

for link in all_links:
    print(link)

