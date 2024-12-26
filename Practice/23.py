import requests
from bs4 import BeautifulSoup
from typing import Iterator, Tuple
from urllib.parse import urljoin

def scrayping() -> Iterator[Tuple[str, str]]:
    url = "https://www.python.org/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        for item in soup.select("div.event-widget li")[:5]:
            tag_title = item.find('a')
            tag_time = item.find('time')
            if tag_title and tag_time:
                event_title = tag_title.text.strip()
                event_date = tag_time.text.strip()
                yield (event_title, event_date)

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        exit()

if __name__ == "__main__":
   for title, date in scrayping():
        print(f'title: {title}')
        print(f'date: {date}')
        print("-" * 50)
