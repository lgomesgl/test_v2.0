from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView

from django.urls import reverse_lazy

from .forms import CreateUserModelForm
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
    Introducing a form with user, first name, last name, gmail, password and password confirmation
    Conect to the User django table
'''
class CreateUserCreateView(CreateView):
    template_name = 'create_user.html'
    model = User
    form_class = CreateUserModelForm
    success_url = reverse_lazy('create_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Novo usuario cadastrado')
        return super(CreateUserCreateView, self).form_valid(form)
    
    
    
