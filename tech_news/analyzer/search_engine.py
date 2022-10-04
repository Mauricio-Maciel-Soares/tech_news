from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    result = [(index["title"], index["url"]) for index in news_list]
    print(result)
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    news_list = search_news({"tag": {"$regex": tag, "$options": "i"}})
    result = [(index["title"], index["url"]) for index in news_list]
    print(result)
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
