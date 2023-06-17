from django.urls import path 
from .views import (HomePageTemplateView, CreateUserCreateView, CreateUserUpdateView, AboutTemplateView, TablesTemplateView, 
                    TablesCreateView, TableListView, TableUpdateView, TableDeleteView, UsersListView)

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('create_user/', CreateUserCreateView.as_view(), name='create_user'),
    # path('create_user/edit', CreateUserUpdateView.as_view(), name='create_user/edit'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('database/', TablesTemplateView.as_view(), name='tables'),
    path('database/<str:table>/add', TablesCreateView.as_view(), name='data-add'),
    path('database/<str:table>/<str:action>', TableListView.as_view(), name='data-list'), # action -> can be view ,update or delete
    # path('database/<str:table>/view', TablesDetailView.asview(), name='tdata-detail'),
    path('database/<str:table>/update/<int:pk>', TableUpdateView.as_view(), name='data-update'),
    path('database/<str:table>/delete/<int:pk>', TableDeleteView.as_view(), name='data-delete'),
    path('users/', UsersListView.as_view(), name='users'),
]
