from django.urls import path 
from .views import (HomePageTemplateView, CreateUserCreateView, CreateUserUpdateView, AboutTemplateView, DatabaseTemplateView, DatabaseDetailView, 
                    DatabaseCreateView, DatabaseListView, DatabaseUpdateView, DatabaseDeleteView, UsersListView)

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('create_user/', CreateUserCreateView.as_view(), name='create_user'),
    # path('create_user/edit', CreateUserUpdateView.as_view(), name='create_user/edit'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('database/', DatabaseTemplateView.as_view(), name='database'),
    path('database/<str:table>/add', DatabaseCreateView.as_view(), name='database-add'),
    path('database/<str:table>/<str:action>', DatabaseListView.as_view(), name='database-list'), # <str:action> -> can be detail, update or delete
    path('database/<str:table>/detail/<int:pk>', DatabaseDetailView.as_view(), name='database-detail'),
    path('database/<str:table>/update/<int:pk>', DatabaseUpdateView.as_view(), name='database-update'),
    path('database/<str:table>/delete/<int:pk>', DatabaseDeleteView.as_view(), name='database-delete'),
    path('users/', UsersListView.as_view(), name='users'),
]
