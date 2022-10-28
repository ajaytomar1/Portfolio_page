from django.db import models

# Create your models here.

class Home(models.Model):
    name= models.CharField(max_length=50)
    greetings1= models.CharField(max_length=10)
    greetings2= models.CharField(max_length=10)
    # picture=models.ImageField(upload_to='picture/')
    
    updated=models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

#about section

class About(models.Model):
    heading = models.CharField(max_length=50)
    career=models.CharField(max_length=50)
    description=models.TextField(blank=False)
    profile_img=models.ImageField(upload_to='profile/')
    updated= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.career

class Profile(models.Model):
    about=models.ForeignKey(About,on_delete=models.CASCADE)
    social_name=models.CharField(max_length=10)
    link=models.URLField(max_length=200)

#skills section

class Category(models.Model):
    name=models.CharField(max_length=20)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural= 'skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    skill_name= models.CharField(max_length=20)

#portfolio section
class Portfolio(models.Model):
    image= models.ImageField(upload_to='portfolio/')
    link= models.URLField(max_length=200)
    desc= models.TextField(blank=True)

    def __str__(self):
        return f'portfolio {self.id}'

# contacts
class Contact(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact_no=models.IntegerField()
    address=models.TextField(max_length= 200)

    def __str__(self):
        return self.name
