from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),          # главная
    path('about/', views.about, name='about'),    # о блоге
    path('post/', views.post, name='post'),       # страница поста
    path('reviews/', views.reviews_view, name='reviews'), # страница отзывов
]
