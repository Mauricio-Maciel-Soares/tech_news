from tech_news.database import search_news


def news_list_result(news_list):
    return [(index["title"], index["url"]) for index in news_list]


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    result = news_list_result(news_list)
    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    news_list = search_news(
        {"tag": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    )
    result = news_list_result(news_list)
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
