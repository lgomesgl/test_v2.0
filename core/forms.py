from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Project, SponsorCompany, People, Email, ReasearchLines, Metadata, Files, Videos, Articles


# Create the forms

# Create user forms
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", 'first_name', 'last_name', 'group']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'over_date']

class SponsorComponyModelForm(forms.ModelForm):
    class Meta:
        model = SponsorCompany
        fields = ['name', 'project']
        
class PeopleModelForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name','sex','post','project']
        
class EmailModelForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['person','type','email']
        
class ReasearchLinesModelForm(forms.ModelForm):
    class Meta:
        model = ReasearchLines
        fields = ['name','phase','point','project','person']
            
class MetadataModelForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = ['title', 'reasearchline', 'contributor', 'contact', 'description', 'keyword', 'notes']
        
class FilesModelForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['metadata','name','type','file','person']
        
class VideosModelForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['metadata','name','video']
        
class ArticlesModelForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['name','link_path','reasearchline','metadata','person']

