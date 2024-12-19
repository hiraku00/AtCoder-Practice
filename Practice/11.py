import requests
from bs4 import BeautifulSoup
from typing import Iterator, Tuple
from urllib.parse import urljoin

def scope_articles(base_url: str = "https://www.python.org/blogs/") -> Iterator[Tuple[str, str]]:
    """
    Args:
        base_url: target of scraping url
    Yields:
        (title, url) of tuple: relative url is converted to absolute url
    Raises:
        requests.exceptions.RequestException: if an errors occurs while accessing the website
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(base_url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for article in soup.select("ul.list-recent-posts li a"):
            title = article.text.strip()
            url = urljoin(base_url, article.get("href"))
            yield (title, url)

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    for title, link in scope_articles():
        print(f"Title: {title}")
        print(f"URL: {link}")
        print("-" * 50)
