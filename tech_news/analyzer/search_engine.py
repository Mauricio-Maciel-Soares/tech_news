from tech_news.database import search_news
from datetime import datetime


def news_list_result(news_list):
    return [(index["title"], index["url"]) for index in news_list]


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    result = news_list_result(news_list)
    return result


# Requisito 7
def search_by_date(date):
    try:
        find_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news_list = search_news(
            {"timestamp": {"$regex": find_date}}
        )
        result = news_list_result(news_list)
        return result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_list = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    )
    result = news_list_result(news_list)
    return result


# Requisito 9
def search_by_category(category):
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    result = news_list_result(news_list)
    return result
