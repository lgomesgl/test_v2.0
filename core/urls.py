from django.urls import path 
from .views import HomePageTemplateView, CreateUserCreateView

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('create_user', CreateUserCreateView.as_view(), name='create_user')
]
