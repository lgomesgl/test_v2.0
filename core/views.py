from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView

from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

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
        context['link_tabelas'] = '/tabelas'
        context['link_usuarios'] = '/users'
        return context 
    
# Create User
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
    
# About
'''
    Just talk about the database and a button to show the correlations of the tables
'''
class AboutTemplateView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_admin'] = '/admin'
        context['link_tables'] = '/tables'
        return context 
    
    
    
