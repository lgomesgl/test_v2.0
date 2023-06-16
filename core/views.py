from typing import Any, Dict, Type
from django import http
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import permission_required
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.db import connection, models
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

from .forms import CustomUserCreationForm, CustomUserChangeForm, ProjectModelForm, SponsorComponyModelForm, PeopleModelForm, EmailModelForm, ReasearchLinesModelForm, MetadataModelForm, FilesModelForm, VideosModelForm, ArticlesModelForm
from .models import CustomUser, Project, SponsorCompany, People, Email, ReasearchLines, Metadata, Files, Videos, Articles

# Create your views here.

# Home page
'''
    TemplateView
    Just show a html
'''
class HomePageTemplateView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_admin'] = '/admin'
        context['link_create_user'] = '/create_user'
        context['link_about'] = '/about'
        context['link_tabelas'] = '/tables'
        context['link_usuarios'] = '/users'
        return context 
    
# -------------------------------------------------- Create User --------------------------------------------------------------------------------------
'''
    CreateView
    Introducing a form with Email, first name, last name, group, password and password confirmation
    Conect to the User django table
'''
class CreateUserCreateView(CreateView):
    template_name = 'create_user.html'
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('create_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'New registered user')
        return super(CreateUserCreateView, self).form_valid(form)
    
class CreateUserUpdateView(UpdateView):
    template_name = 'create_user.html'
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('create_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'New registered user')
        return super(CreateUserCreateView, self).form_valid(form)
    
# -------------------------------------------------- About ----------------------------------------------------------------------------------------------
'''
    Just talk about the database and a button to show the correlations of the tables
'''
class AboutTemplateView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_admin'] = '/admin'
        context['link_home'] = 'http://127.0.0.1:8000/'
        context['link_tables'] = '/tables'
        return context 
    
# ------------------------------------------------- Tables --------------------------------------------------------------------------------------------
'''
    Show the tables and link with create/update/delete instances for each tables
'''
class TablesTemplateView(TemplateView):
    '''
        Permissions
    '''
    template_name = 'tables.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_home'] = 'http://127.0.0.1:8000/'
        context['link_about'] = '/about'
        context['link_admin'] = '/admin'
        
        # tables = connection.introspection.table_name()
        # seen_models = connection.introspection.installed_models(tables)
        
        context['tables'] = []
        tables = ['project','sponsor_compony','people','email','reasearch_lines','metadata','files','videos','articles']      
        for table in tables:
            context['tables'].append({'nome':'%s' % table, 'link_view':'', 'link_create':'tables/%s/add' % table,
                                      'link_update':'tables/%s/update' % table, 'link_delete':'tables/%s/delete' % table})

        return context 
  
# Tables/view

# Tables/create
'''
    One view which works for all create forms.
'''
class TablesCreateView(CreateView):
    template_name = 'tables_create.html'
    
    def get(self, request, *args, **kwargs):
        '''
            Get from URL the table 
        '''
        self.object = None
        self.table = kwargs['table']
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['table'] = self.table     
        return context 
      
    def get_form_class(self):
        FORMS = {
            "project": ProjectModelForm,
            "sponsor_compony": SponsorComponyModelForm,
            "people": PeopleModelForm,
            "email": EmailModelForm,
            "reasearch_lines": ReasearchLinesModelForm,
            "metadata": MetadataModelForm,
            "files": FilesModelForm,
            "videos": VideosModelForm,
            "articles": ArticlesModelForm,
        }
        self.form_class = FORMS[self.table]
        return super().get_form_class()
    
    def get_queryset(self):
        MODELS = {
            "project": Project,
            "sponsor_compony": SponsorCompany,
            "people": People,
            "email": Email,
            "reasearch_lines": ReasearchLines,
            "metadata": Metadata,
            "files": Files,
            "videos": Videos,
            "articles": Articles,
        }
        self.model = MODELS[self.table]
        return super().get_queryset()
     
    def post(self, request, *args, **kwargs):
        self.object = None
        self.table = kwargs['table']        
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'New registered user')
        return super(TablesCreateView, self).form_valid(form)
    
    def form_invalid(self, form): 
        messages.error(self.request, 'Erro to register') 
        return super(TablesCreateView, self).form_invalid(form)
    
    def get_success_url(self):
        self.success_url = self.request.path
        return super().get_success_url()
    
# Table/update
class TableListView(ListView):
    '''
        First show all instances in table.
        Link the path to TableUpdateView
    '''
    template_name = 'tables_view.html'
    
    def get(self, request, *args, **kwargs):
        self.object = None
        self.table = kwargs['table']
        self.action = kwargs['action']
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        MODELS = {
            "project": Project,
            "sponsor_compony": SponsorCompany,
            "people": People,
            "email": Email,
            "reasearch_lines": ReasearchLines,
            "metadata": Metadata,
            "files": Files,
            "videos": Videos,
            "articles": Articles,
        }
        self.model = MODELS[self.table]
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_home'] = '/'
        context['tables'] = '/tables'
        context['table'] = self.table
        context['action'] = self.action
        context['instances'] = self.model.objects.all()
        return context

class TableUpdateView(UpdateView):
    '''
        Get the id of the instance and update in model
    '''
    template_name = 'tables_update.html'
    fields = "__all__"
    
    def get(self, request, *args, **kwargs):
        self.object = None
        self.table = kwargs['table']
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        MODELS = {
            "project": Project,
            "sponsor_compony": SponsorCompany,
            "people": People,
            "email": Email,
            "reasearch_lines": ReasearchLines,
            "metadata": Metadata,
            "files": Files,
            "videos": Videos,
            "articles": Articles,
        }
        self.model = MODELS[self.table]
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = self.table
        return context
    
    def post(self, request, *args, **kwargs):
        self.table = kwargs['table']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Update completed')
        return super(TableUpdateView, self).form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Erro to update')
        return super().form_invalid(form)
    
    def get_success_url(self):
        self.success_url = self.request.path
        return super().get_success_url()
    
class TableDeleteView(DeleteView):
    '''
        Delete the instance of table
    '''
    template_name = 'tables_delete.html'
    
    def get(self, request, *args, **kwargs):
        self.object = None
        self.table = kwargs['table']
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        MODELS = {
        "project": Project,
        "sponsor_compony": SponsorCompany,
        "people": People,
        "email": Email,
        "reasearch_lines": ReasearchLines,
        "metadata": Metadata,
        "files": Files,
        "videos": Videos,
        "articles": Articles,
    }
        self.model = MODELS[self.table]
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = self.table
        context['name'] = self.model.objects.all().get(id=self.kwargs.get(self.pk_url_kwarg))
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None
        self.table = kwargs['table']
        return super().post(request, *args, **kwargs)
    
    def get_success_url(self, **kwargs):
        self.success_url = reverse_lazy('tables-list', kwargs = {'table': self.table, 'action': 'delete'})
        return super().get_success_url()
    
# ---------------------------------- users ----------------------------------------------------
'''
    ListView or DetailView??
'''
class UsersListView(ListView):
    pass