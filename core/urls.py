from django.urls import path 
from .views import HomePageTemplateView, CreateUserCreateView, CreateUserUpdateView, AboutTemplateView, TablesTemplateView, TablesCreateView

from .models import Metadata
from .forms import MetadataModelForm

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('create_user', CreateUserCreateView.as_view(), name='create_user'),
    # path('create_user/edit', CreateUserUpdateView.as_view(), name='create_user/edit'),
    path('about', AboutTemplateView.as_view(), name='about'),
    path('tables', TablesTemplateView.as_view(), name='tables'),
    # path('tables/<str:table>/view', TablesListView.asview(), name='tables/<table>/view'),
    path('tables/<str:table>/add', TablesCreateView.as_view(), name='tables/<table>/add'),
]
