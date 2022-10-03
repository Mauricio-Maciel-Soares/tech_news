from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        for _ in range(15):
            response = requests.get(
                url, timeout=3, headers={"user-agent": "Fake user-agent"}
            )
            time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css("h2.entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".next::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    content = {}
    selector = Selector(text=html_content)
    content["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    suffix = "\xa0\xa0\xa0"
    if title.endswith(suffix):
        content["title"] = title[:-len(suffix)]
    else:
        content["title"] = title
    content["timestamp"] = selector.css(".meta-date::text").get()
    content["writer"] = selector.css("a.url::text").get()
    content["comments_count"] = len(
        selector.css("div.comment-body::text").getall()
    )
    content["summary"] = "".join(
        selector.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()
    content["tags"] = selector.css("section.post-tags a::text").getall()
    content["category"] = selector.css("span.label::text").get()

    return content


# Requisito 5
def get_tech_news(amount):
    data = []
    url = "https://blog.betrybe.com/"
    html_content = fetch(url)

    while True:
        link_content = scrape_novidades(html_content)
        for index in link_content:
            result = scrape_noticia(fetch(index))
            data.append(result)
            if len(data) == amount:
                create_news(data)
                return data
        next_url = scrape_next_page_link(html_content)
        html_content = fetch(next_url)
