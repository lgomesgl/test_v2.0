from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Project, SponsorCompany, People, Email, ReasearchLines, Videos, Metadata, Files, Articles

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'Over date']
    search_fields = ['name']
    
@admin.register(SponsorCompany)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(People)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','Post']
    list_filter = ['Post']
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

# @admin.register(CustomUser)
# class CustomUser(UserAdmin):
#     pass
    
    