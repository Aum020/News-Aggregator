import requests
from django.shortcuts import render
from newsapp.models import Article, Sports, Entertainment, Politics
from newsapp.news import render_news, render_pol_news, render_sports, render_ent_news
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def send_politics_news(request):
    url = "https://newsapi.org/v2/everything?q=Politics&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    news = requests.get(url).json()
    article = news["articles"]
    if __name__ == "__main__":
        render_pol_news(article)
    headline = Politics.objects.all()
    context = paginate(headline, request)
    return render(request, "newsapp/Politics.html", context)

def send_india_news(request):
    india_url = "https://newsapi.org/v2/everything?q=India&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_india_page = requests.get(india_url).json()
    article = open_india_page["articles"]
    if __name__ == "__main__":
        render_news(article)
    headline = Article.objects.all()
    context = paginate(headline, request)
    return render(request,"newsapp/Frontpage.html", context)


def send_sports_news(request):
    sports_url = "https://newsapi.org/v2/everything?q=Sports&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_sports_page = requests.get(sports_url).json()
    article = open_sports_page["articles"]
    if __name__ == "__main":
        render_sports(article)
    headline = Sports.objects.all()
    context = paginate(headline, request)
    return render(request, "newsapp/Sports.html", context)



def send_entertainment_news(request):
    ent_url = "https://newsapi.org/v2/everything?q=Entertainment&pageSize=100&apiKey=4f784078aec04d8d96fe1d1e1e4281bb"
    open_ent_page = requests.get(ent_url).json()
    article = open_ent_page["articles"]
    if __name__ == "__main__":
        render_ent_news(article)
    headline = Entertainment.objects.all()
    context = paginate(headline, request)
    return render(request, "newsapp/Entertainment.html", context)

def paginate(headline, request):
    paginator = Paginator(headline, 20)
    page = request.GET.get('page')
    try:
        pageno = paginator.page(page)
    except PageNotAnInteger:
        pageno = paginator.page(1)
    except EmptyPage:
        pageno = paginator.page(paginator.num_pages)
    context = {
        'object_list': pageno,
    }
    return context

