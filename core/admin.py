from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Project, SponsorCompany, People, Email, ReasearchLines, Videos, Metadata, Files, Articles, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "first_name", "last_name", "group", "is_superuser"]
    list_filter = ["group", "is_superuser"]
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'group')}),
        ('Permissôes', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Data Importantes', {'fields': ('last_login', 'date_joined')}),   
    ]
    search_fields = ["email", "first_name"]
    ordering = ["email"] # necessary because the django order default by username, and we change the username for email.
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'over_date']
    search_fields = ['name']
    
@admin.register(SponsorCompany)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(People)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','position']
    list_filter = ['position']
    search_fields = ['name']

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['person', 'type', 'email'] # person is a id number -> try to give the name of instance id
    search_fields = ['person']
    
@admin.register(ReasearchLines)
class ReaseachAdmin(admin.ModelAdmin):
    list_display = ['name','phase','point']
    search_fields = ['name','phase','point']
    
@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'keyword']
                                                            
@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['file', 'type', 'metadata']
    search_fields = ['file', 'type', 'metadata']

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
