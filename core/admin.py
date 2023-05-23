from django.contrib import admin

from .models import Project, Enterprise, Person, Email, Reasearch, Videos, Metadata, Files

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'Over date']
    search_fields = ['name']
    
@admin.resgister(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'post']
    search_fields = ['name']

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['person', 'type', 'email'] # person is a id number -> try to give the name of instance id
    search_fields = ['person']
    
@admin.register(Reasearch)
class ReaseachAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
                                                            
@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    
    