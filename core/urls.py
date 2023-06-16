from django.urls import path 
from .views import (HomePageTemplateView, CreateUserCreateView, CreateUserUpdateView, AboutTemplateView, TablesTemplateView, 
                    TablesCreateView, TableListView, TableUpdateView, TableDeleteView)

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('create_user', CreateUserCreateView.as_view(), name='create_user'),
    # path('create_user/edit', CreateUserUpdateView.as_view(), name='create_user/edit'),
    path('about', AboutTemplateView.as_view(), name='about'),
    path('tables', TablesTemplateView.as_view(), name='tables'),
    # path('tables/<str:table>/view', TablesListView.asview(), name='tables/<table>/view'),
    path('tables/<str:table>/add', TablesCreateView.as_view(), name='tables-add'),
    path('tables/<str:table>/<str:action>', TableListView.as_view(), name='tables-list'), # action -> can be update or delete
    path('tables/<str:table>/update/<int:pk>', TableUpdateView.as_view(), name='tables-update'),
    path('tables/<str:table>/delete/<int:pk>', TableDeleteView.as_view(), name='tables-delete'),
    # path('users', )
]
