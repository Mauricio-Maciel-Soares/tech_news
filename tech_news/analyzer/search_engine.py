from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result_news = []
    result_search = search_news({"title": {"$regex": "t"}})
    for title in result_search:
        result_news.append(title["title"], title["url"])
    print(result_news)
    return result_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
