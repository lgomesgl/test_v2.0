from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group

# Create your models here
class Base(models.Model):
    '''
    Table with some ordinary columns that we wanted in some tables. 
    '''
    creates_date = models.DateField(name='Creates date', auto_now_add=True)
    modify_date = models.DateField(name='Modify date', auto_now=True)
    
    class Meta:
        abstract = True
        
class Project(Base):
    name = models.CharField(max_length=100, unique=True)
    over_date = models.DateField(name='Over date', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'
    
class SponsorCompany(Base):
    name = models.CharField(max_length=100, unique=True)
    project = models.ManyToManyField(Project)
    
    def __str__(self):
        return self.name   
    
    class Meta:
        verbose_name = 'SponsorCompany'
        verbose_name_plural = 'SponsorCompany'
    
class People(Base):
    SEX = [
        #('DataBase','Form')
        ('M','Masculino'),
        ('F','Feminino'),    
    ]
    
    POST = [
        ('Professor Doutor','Professor Doutor'),
        ('Professor Adjunto','Professor Adjunto'),
        ('Pesquisador','Pesquisador'),
        ('Pós-Doc','Pós-Doc'),
        ('Doutorando','Doutorando'),
        ('Mestrando','Mestrando'),
        ('Iniciação científica','Iniciação científica'),
    ]
    
    name = models.CharField(max_length=100)
    sex = models.CharField(name='Sex', max_length=1, choices=SEX)
    post = models.CharField(name='Post', max_length=50, choices=POST)
    projeto = models.ManyToManyField(Project)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'People'
        verbose_name_plural = 'People'

class Email(Base):
    TYPE = [
        ('Pessoal','Pessoal'),
        ('Educacional','Educacional'),
    ]
     
    type = models.CharField(max_length=15, choices=TYPE)
    email = models.EmailField(max_length=50)
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Email'
        
class ReasearchLines(Base):
    PHASE = [
        ('Single-phase-flow','Single-phase-flow'),
        ('Two-phase-flow','Two-phase-flow'),
        ('Three-phase-flow','Three-phase-flow'),
    ]
    
    name = models.CharField(max_length=50)
    phase = models.CharField(max_length=30, blank=True, choices=PHASE)
    point = models.CharField(max_length=50, blank=True)
    
    project = models.ManyToManyField(Project)
    person = models.ManyToManyField(People)
    
    def __str__(self):
        '''
            The ReasearchLines can be separeted with two properties(phase and point)
        '''
        if not self.phase == '':
            return '%s-%s' %(self.name, self.phase)
        else: 
            return '%s-%s' %(self.name, self.point)
    
    class Meta:
        verbose_name = 'ReasearchLines'
        verbose_name_plural = 'ReasearchLines'
          
class Metadata(Base):
    title = models.CharField(max_length=100, default='')
    reasearchline = models.ForeignKey(ReasearchLines, null=True, blank=True, on_delete=models.CASCADE)
    contributor = models.ManyToManyField(People)
    contact = models.ManyToManyField(Email)
    description = models.TextField(blank=True)
    keyword = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Metadata'
        verbose_name_plural = 'Metadata'
        
class Files(Base):
    TYPE = [
        ('PDF','PDF'),
        ('EXCEL','EXCEL'),
        ('WORD','WORD'),    
    ]
     
    metadata = models.ForeignKey(Metadata, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, blank=True, choices=TYPE)
    file = models.FileField(blank=True)
    
    # reasearchline = models.ForeignKey(ReasearchLines, on_delete=models.CASCADE)
    person = models.ManyToManyField(People)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Files'
        verbose_name_plural = 'Files'   
    
class Videos(Base):
    metadata = models.ForeignKey(Metadata, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    video = models.FileField(blank=True)
    
    # reasearchline = models.ForeignKey(ReasearchLines, on_delete=models.CASCADE)
    # file = models.ManyToManyField(Files)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Videos'
        verbose_name_plural = 'Videos'   
        
class Articles(Base):
    name = models.CharField(max_length=50)
    link_path = models.CharField(max_length=100)
    
    reasearchline = models.ForeignKey(ReasearchLines, null=True, blank=True, on_delete=models.CASCADE)
    metadata = models.ManyToManyField(Metadata)
    # file = models.ManyToManyField(Files)
    # videos = models.ManyToManyField(Videos)
    person = models.ManyToManyField(People)
  
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Articles'     
        
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    '''
        Show all groups that we have in group django table 
        *Admin can be not necessary
    '''
    # GROUP = Group.objects.all() ## get all groups in django database
    GROUP = [
        ('Admin','Admin'),
        ('SponsorCompony','SponsorCompony'),
        ('IC','IC'),
    ]
    
    username = None
    email = models.EmailField("email address", unique=True)
    group = models.CharField(max_length=50, blank=True, choices=GROUP)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'group']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
    