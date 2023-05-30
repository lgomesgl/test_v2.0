from django.urls import path 
from .views import HomePageTemplateView, CreateUserCreateView, AboutTemplateView

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('create_user', CreateUserCreateView.as_view(), name='create_user'),
    path('about', AboutTemplateView.as_view(), name='about')
]
