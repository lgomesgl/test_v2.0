from typing import Any, Dict, Type
from django import http
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import permission_required
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.db import connection, models
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

from .forms import CustomUserCreationForm, CustomUserChangeForm, ProjectModelForm, SponsorComponyModelForm, PeopleModelForm, EmailModelForm, ReasearchLinesModelForm, MetadataModelForm, FilesModelForm, VideosModelForm, ArticlesModelForm
from .models import CustomUser, Project, SponsorCompany, People, Email, ReasearchLines, Metadata, Files, Videos, Articles

# Create your views here.

# --------------------------------------------------- Home page ---------------------------------------------------------------
'''
    TemplateView
    Just show a the home page with all acess
'''
class HomePageTemplateView(TemplateView):
    template_name = 'home_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_admin'] = '/admin'
        context['link_create_user'] = '/create_user'
        context['link_about'] = '/about'
        context['link_database'] = '/database'
        context['link_users'] = '/users'
        
        context['databases_detail'] = []
        tables = ['project','sponsor_compony','people','email','reasearch_lines','metadata','files','videos','articles']      
        for table in tables:
            context['databases_detail'].append({'nome':'%s' % table, 'link_detail':'database/%s/detail' % table})
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
        context['link_create_user'] = '/create_user'
        context['link_database'] = '/database'
        context['link_users'] = '/users'
        
        context['databases_detail'] = []
        tables = ['project','sponsor_compony','people','email','reasearch_lines','metadata','files','videos','articles']      
        for table in tables:
            context['databases_detail'].append({'nome':'%s' % table, 'link_detail':'database/%s/detail' % table})
            
        return context 
    
# ------------------------------------------------- Tables --------------------------------------------------------------------------------------------
'''
    Show the tables and link with create/update/delete instances for each tables
'''
class DatabaseTemplateView(TemplateView):
    '''
        Permissions
    '''
    template_name = 'database.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_home'] = 'http://127.0.0.1:8000/'
        context['link_about'] = '/about'
        context['link_admin'] = '/admin'
        context['link_users'] = '/users'
        
        # tables = connection.introspection.table_name()
        # seen_models = connection.introspection.installed_models(tables)
        
        context['tables'] = []
        tables = ['project','sponsor_compony','people','email','reasearch_lines','metadata','files','videos','articles']      
        for table in tables:
            context['tables'].append({'nome':'%s' % table, 'link_view':'', 'link_create':'%s/add' % table,
                                      'link_update':'%s/update' % table, 'link_delete':'%s/delete' % table})

        return context 
  
# Tables/detail
'''
    Template with the datails of the instance
'''
class DatabaseDetailView(DetailView):
    template_name = 'database_detail.html'
    
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
    
# Tables/create
'''
    One view which works for all create forms.
'''
class DatabaseCreateView(CreateView):
    template_name = 'database_create.html'
    
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
        messages.success(self.request, 'New %s registered' % self.table )
        return super(DatabaseCreateView, self).form_valid(form)
    
    def form_invalid(self, form): 
        messages.error(self.request, 'Erro to register') 
        return super(DatabaseCreateView, self).form_invalid(form)
    
    def get_success_url(self):
        self.success_url = self.request.path
        return super().get_success_url()
    
# Table/update
class DatabaseListView(ListView):
    '''
        First show all instances in table.
        Link the path to TableUpdateView
    '''
    template_name = 'database_list.html'
    
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
        context['link_about'] = '/about'
        context['link_tables'] = '/database'
        context['table'] = self.table
        context['action'] = self.action
        context['instances'] = self.model.objects.all()
        return context

class DatabaseUpdateView(UpdateView):
    '''
        Get the id of the instance and update in model
    '''
    template_name = 'database_update.html'
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
        return super(DatabaseUpdateView, self).form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Erro to update')
        return super(DatabaseUpdateView, self).form_invalid(form)
    
    def get_success_url(self):
        self.success_url = self.request.path
        return super().get_success_url()
    
class DatabaseDeleteView(DeleteView):
    '''
        Delete the instance of table
    '''
    template_name = 'database_delete.html'
    
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
        context['name_of_delete_instance'] = self.model.objects.all().get(id=self.kwargs.get(self.pk_url_kwarg))
        return context
    
    def form_valid(self, form):
        messages.success(self.request, '%s deleted' % (self.model.objects.all().get(id=self.kwargs.get(self.pk_url_kwarg))))
        return super(DatabaseDeleteView, self).form_valid(form)   
    
    def post(self, request, *args, **kwargs):
        self.object = None
        self.table = kwargs['table']
        return super().post(request, *args, **kwargs)
    
    def get_success_url(self, **kwargs):
        self.success_url = reverse_lazy('database-list', kwargs = {'table': self.table, 'action': 'delete'})
        return super().get_success_url()
    
# ---------------------------------- users ----------------------------------------------------
'''
    ListView  -> List all users in DBA
'''
class UsersListView(ListView):
    template_name = 'users.html'
    
    def get_queryset(self):
        self.model = CustomUser
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index'] = 'home'
        context['link_admin'] = '/admin'
        context['link_about'] = '/about'
        context['link_database'] = '/database'
        context['usuarios'] = self.model.objects.all()
        return context
    