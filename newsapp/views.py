
from django.shortcuts import render
from django.db.models import Q
from itertools import chain
from newsapp.models import Article, Sports, Entertainment, Politics
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def send_politics_news(request):
    headline = Politics.objects.get_queryset().order_by('id')
    context = paginate(headline, request)
    return render(request, "newsapp/Politics.html", context)


def send_india_news(request):
    headline = Article.objects.get_queryset().order_by('id')
    context = paginate(headline, request)
    return render(request, "newsapp/Frontpage.html", context)


def send_sports_news(request):
    headline = Sports.objects.get_queryset().order_by('id')
    context = paginate(headline, request)
    return render(request, "newsapp/Sports.html", context)


def send_entertainment_news(request):
    headline = Entertainment.objects.get_queryset().order_by('id')
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
def search(request):
    template = "newsapp/search.html"
    query = request.GET.get('q')
    india = Article.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    ent = Entertainment.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    pol = Politics.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    sports = Sports.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    page = list(
        sorted(
            chain(india, ent, pol, sports),
            key= lambda objects:objects.title
        )
    )
    context = paginate(page, request)

    return render(request, template, context)
