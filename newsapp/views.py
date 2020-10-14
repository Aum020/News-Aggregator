from django.shortcuts import render
from newsapp.models import Article, Sports, Entertainment, Politics
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def send_politics_news(request):
    headline = Politics.objects.all()
    context = paginate(headline, request)
    return render(request, "newsapp/Politics.html", context)


def send_india_news(request):
    headline = Article.objects.all()
    context = paginate(headline, request)
    return render(request, "newsapp/Frontpage.html", context)


def send_sports_news(request):
    headline = Sports.objects.all()
    context = paginate(headline, request)
    return render(request, "newsapp/Sports.html", context)


def send_entertainment_news(request):
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
