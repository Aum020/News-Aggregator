from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.send_india_news, name="send_news"),
                  path('Sports/', views.send_sports_news, name="send_sports_news"),
                  path('Entertainment/', views.send_entertainment_news, name="send_entertainment_news"),
                  path('Politics/', views.send_politics_news, name="send_politics_news"),
                  path('Results/', views.search, name="search")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
