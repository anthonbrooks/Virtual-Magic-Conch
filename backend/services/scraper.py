import requests
from bs4 import BeautifulSoup

def extract_text(url):
    try:
        html = requests.get(url, timeout=5).text
        soup = BeautifulSoup(html, "html.parser")

        paragraphs = soup.find_all("p")

        return " ".join(p.get_text() for p in paragraphs)[:4000]

    except:
        return ""


def gather_context(urls):

    articles = []

    for url in urls:
        text = extract_text(url)
        if text:
            articles.append(text)

    return "\n\n".join(articles)