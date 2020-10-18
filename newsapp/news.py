import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "News.settings")
django.setup()
import requests
from newsapp.models import Article, Sports, Entertainment, Politics


def render_news():
    india_url = "https://newsapi.org/v2/everything?q=India&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_india_page = requests.get(india_url).json()
    ind_article = open_india_page["articles"]
    for ar in ind_article:
        news_headlines = Article()
        news_headlines.title = ar["title"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        exists = False
        for news in Article.objects.all():
            if news.desc == news_headlines.desc:
                exists = True
                print(news.desc)
                break
        if not exists:
            news_headlines.save()


def render_pol_news():
    pol_url = "https://newsapi.org/v2/everything?q=Politics&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    news = requests.get(pol_url).json()
    pol_article = news["articles"]
    for ar in pol_article:
        news_headlines = Politics()
        news_headlines.title = ar["title"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        exists = False
        for news in Politics.objects.all():
            if news.desc == news_headlines.desc:
                exists = True
                break
        if not exists:
            news_headlines.save()


def render_sports_news():
    sports_url = "https://newsapi.org/v2/everything?q=Sports&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_sports_page = requests.get(sports_url).json()
    sports_article = open_sports_page["articles"]
    for ar in sports_article:
        news_headlines = Sports()
        news_headlines.title = ar["title"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        exists = False
        for news in Sports.objects.all():
            if news.desc == news_headlines.desc:
                exists = True
                break
        if not exists:
            news_headlines.save()


def render_ent_news():
    ent_url = "https://newsapi.org/v2/everything?q=Entertainment&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_ent_page = requests.get(ent_url).json()
    article = open_ent_page["articles"]
    for ar in article:
        news_headlines = Entertainment()
        news_headlines.title = ar["title"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        exists = False
        for news in Entertainment.objects.all():
            if news.title == news_headlines.title or news.desc == news_headlines.desc:
                exists = True
                break
        if not exists:
            news_headlines.save()


if __name__ == "__main__":
    render_news()
    render_pol_news()
    render_ent_news()
    render_sports_news()
