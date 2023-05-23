from django.db import models

# Create your models here.
'''
    -- att the columns in tables
    -- put the BLOB fields in tables
    -- test the 1xN/NxN relations
    -- view  on_delete types
'''
class Base(models.Model):
    creates_date = models.DateField(name='Creates date', auto_now_add=True)
    modify_date = models.DateField(name='Modify date', auto_now=True)
    # modify_user = models.CharField()
    
    class Meta:
        abstract = True
        
class Project(Base):
    name = models.CharField(max_length=True, unique=True)
    over_date = models.DateField(name='Over date', null=True, blanck=True)
    
    def __str__(self):
        return self.name
    
class Enterprise(Base):
    name = models.CharField(max_length=100, unique=True)
    project = models.ManyToManyField(Project)
    
    def __str__(self):
        return self.name   
    
class Person(Base):
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
    post = models.CharField(name='Post', max_length=100, choices=POST)
    projeto = models.ManyToManyField(Project)
    
    def __str__(self):
        return self.name

class Email(Base):
    type = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email
    
class Reasearch(Base):
    name = models.CharField(max_length=50)
    idperson = models.ManyToManyField(Person)
    
    def __str__(self):
        return self.name
          
class Videos(Base):
    name = models.CharField(max_length=50)
    # videos = BLOB
    idreasearch = models.ForeignKey(Reasearch, on_delete=models.CASCADE)
    
class Metadata(Base):
    name = models.CharField(max_length=50)
    # file = BLOB
    idreasearch = models.ForeignKey(Reasearch, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Videos)
    
class Files(Base):
    name = models.CharField(max_length=50)
    # file = BLOB
    idreasearch = models.ForeignKey(Reasearch, on_delete=models.CASCADE)
    idmetadata = models.ForeignKey(Metadata, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Videos)
    
class Articles(Base):
    name = models.CharField(max_length=50)
    link_path = models.CharField(max_length=100)
    idreasearch = models.ForeignKey(Reasearch, on_delete=models.CASCADE)
    files = models.ManyToManyField(Files)
    videos = models.ManyToManyField(Videos)
    metadata = models.ManyToManyField(Metadata)
    person = models.ManyToManyField(Person)
    
    
    