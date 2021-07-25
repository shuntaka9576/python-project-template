from typing import List, Optional, TypedDict


class DbArticle(TypedDict):
    title: str
    user_id: str
    extra_field1: str
    extra_field2: str


class Article(TypedDict):
    title: str
    user_id: str


def get_articles_from_db(userId: str) -> Optional[List[DbArticle]]:
    return None


def get_articles(user_id: str) -> List[Article]:
    db_article_list = get_articles_from_db(user_id)
    article_list: List[Article] = []

    if db_article_list is None:
        return []
    else:
        for db_article in db_article_list:
            article: Article = {
                "title": db_article["title"],
                "user_id": db_article["user_id"],
            }
            article_list.append(article)

        return article_list


if __name__ == "__main__":
    user_id = "alice"
    article_list = get_articles(user_id)

    if len(article_list) == 0:
        print("Not found article")
    else:
        print(article_list)
