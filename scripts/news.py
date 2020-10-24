import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "News.settings")
django.setup()
import newspaper
import requests
from newsapp.models import Article, Sports, Entertainment, Politics


def render_news():
    india_url = "https://newsapi.org/v2/everything?q=India&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_india_page = requests.get(india_url).json()
    ind_article = open_india_page["articles"]
    i = 0
    for ar in ind_article:
        news_headlines = Article()
        news_headlines.title = ar["title"]
        news_headlines.name = ind_article[i]['source']['name']
        news_headlines.url = ar["url"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        if ar["urlToImage"] is None:
            news_headlines.img = downloadimg(ar["url"])
        exists = False
        for news in Article.objects.all():
            if news.desc == ar["description"]:
                exists = True
                break
        if not exists:
            news_headlines.save()
        i+=1


def render_pol_news():
    pol_url = "https://newsapi.org/v2/everything?q=Indian%20Politics&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    news = requests.get(pol_url).json()
    pol_article = news["articles"]
    for ar in pol_article:
        news_headlines = Politics()
        news_headlines.title = ar["title"]

        news_headlines.url = ar["url"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        if ar["urlToImage"] is None:
            news_headlines.img = downloadimg(ar["url"])
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

        news_headlines.url = ar["url"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        if ar["urlToImage"] is None:
            news_headlines.img = downloadimg(ar["url"])
        exists = False
        for news in Sports.objects.all():
            if news.desc == news_headlines.desc:
                exists = True
                break
        if not exists:
            news_headlines.save()


def render_ent_news():
    ent_url = "https://newsapi.org/v2/everything?q=Indian%20Entertainment&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_ent_page = requests.get(ent_url).json()
    article = open_ent_page["articles"]
    for ar in article:
        news_headlines = Entertainment()
        news_headlines.title = ar["title"]

        news_headlines.url = ar["url"]
        news_headlines.img = ar["urlToImage"]
        news_headlines.desc = ar["description"]
        if ar["urlToImage"] is None:
            news_headlines.img = downloadimg( ar["url"])
        exists = False
        for news in Entertainment.objects.all():
            if  news.desc == ar["description"]:
                exists = True
                break
        if not exists:
            news_headlines.save()


def downloadimg(img_url):
    url = img_url
    news = newspaper.Article(url)
    news.download()
    try:
        news.parse()
        return news.top_image
    except newspaper.ArticleException:
        return None

def run():
    render_news()
    render_pol_news()
    render_ent_news()
    render_sports_news()
