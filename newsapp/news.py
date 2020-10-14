from newsapp.models import Article, Sports, Politics, Entertainment

def render_news(article):
    for ar in article:
        new_article = Article()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()

def render_sports(article):

    for ar in article:
        new_article = Sports()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()
def render_ent_news(article):
    for ar in article:
        new_article = Entertainment()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()

def render_pol_news(article):
    for ar in article:
        new_article = Politics()
        new_article.title = ar["title"]
        new_article.desc = ar["description"]
        new_article.img = ar["urlToImage"]
        new_article.save()