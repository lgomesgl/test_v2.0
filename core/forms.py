from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Project, SponsorCompany, People, Email, ReasearchLines, Metadata, Files, Videos, Articles


# Create the forms
'''
    Upload many files in FilesModelForm

'''

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
        
        # if (Project.objects.all().count()) < 5:
        #     widget = forms.CheckboxSelectMultiple
        # else:
        #     widget = None
        
        # project = forms.ModelMultipleChoiceField(
        #     queryset= Project.objects.all(),
        #     widget = widget
        # )
        
class PeopleModelForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['name','sex','position','project']
        
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
        
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
        
class FilesModelForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['metadata','name','type','file','person']
        
        file = MultipleFileInput()
        
class VideosModelForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['metadata','name','video']
        
class ArticlesModelForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['name','link_path','reasearchline','metadata','person']

