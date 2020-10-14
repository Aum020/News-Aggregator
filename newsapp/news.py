import requests
from newsapp.models import Article, Sports, Politics, Entertainment

india_url = "https://newsapi.org/v2/everything?q=India&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
open_india_page = requests.get(india_url).json()
article = open_india_page["articles"]

sports_url = "https://newsapi.org/v2/everything?q=Sports&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
open_sports_page = requests.get(sports_url).json()
sports_article = open_sports_page["articles"]

ent_url = "https://newsapi.org/v2/everything?q=Entertainment&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
open_ent_page = requests.get(ent_url).json()
ent_article = open_ent_page["articles"]

url = "https://newsapi.org/v2/everything?q=Politics&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
news = requests.get(url).json()
pol_article = news["articles"]


def render_news():
    for ar in article:
        new_article = Article()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()


def render_sports():
    for ar in sports_article:
        new_article = Sports()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()


def render_ent_news():
    for ar in ent_article:
        new_article = Entertainment()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()


def render_pol_news():
    for ar in pol_article:
        new_article = Politics()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()


if __name__ == "__main__":
    render_news()
    render_sports()
    render_ent_news()
    render_pol_news()
