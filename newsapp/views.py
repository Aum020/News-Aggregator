import requests
from django.http import HttpResponse
from django.shortcuts import render
from GoogleNews import GoogleNews
from newspaper import Article, ArticleException


# Create your views here.

def send_politics_news(request):
    url = ('http://newsapi.org/v2/everything?'
           'q=Politics&'
           'language = en'
           'from=2020-10-10&'
           'sortBy=popularity&'
           'apiKey=4f784078aec04d8d96fe1d1e1e4281bb')
    news = requests.get(url).json()
    article = news["articles"]
    my_list = render_news(article, request, "newsapp/Politics.html")
    return my_list


def send_category(request, category):
    page = category + ".html"
    return HttpResponse(page)


def send_india_news(request):
    india_url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_india_page = requests.get(india_url).json()
    article = open_india_page["articles"]
    my_list = render_news(article, request, "newsapp/Frontpage.html")
    return my_list


def send_sports_news(request):
    sports_url = "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_sports_page = requests.get(sports_url).json()
    article = open_sports_page["articles"]
    my_list = render_news(article, request, "newsapp/Sports.html")
    return my_list


def send_entertainment_news(request):
    ent_url = "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_ent_page = requests.get(ent_url).json()
    article = open_ent_page["articles"]
    my_list = render_news(article, request, "newsapp/Entertainment.html")
    return my_list


def render_news(article, request, file):
    desc = []
    title = []
    img = []

    for ar in article:
        title.append(ar["title"])
        img.append(ar["urlToImage"])
        desc.append(ar["description"])

    my_list = zip(title, desc, img)
    return render(request, file, context={"my_list": my_list})


def render_custom(request, urls, file):
    # urls = list(dict.fromkeys(urls))
    desc = []
    title = []
    img = []
    for url in urls:
        try:
            article = Article(url)
            print(url)
            article.download()
            article.parse()
            article.nlp()
        except ArticleException:
            continue
        else:
            img.append(article.top_img)
            desc.append(article.summary)
            title.append(article.title)
        # print(Surat.top_image)
        # print(Surat.summary)
    my_list = zip(title, img, desc)
    return render(request, file, context={"my_list": my_list})
