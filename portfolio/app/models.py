from django.db import models

# Create your models here.
class Contactus(models.Model):
    Name = models.CharField(max_length=30,default="anonymous")
    Email = models.EmailField()
    Phone = models.BigIntegerField(null=False)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Name
    
class Filefield(models.Model):
    file = models.FileField(upload_to="static/file")
    title = models.CharField(max_length=255,default="title")

    def __str__(self):
        return self.title

class Eduction(models.Model):
    title = models.CharField(max_length=150,default="title1")
    school_name = models.CharField(max_length=255,default="Igmp")
    university_name = models.CharField(max_length=255,default="HPBS")
    location = models.CharField(max_length=50,default="Dehra")
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Course(models.Model):
    image = models.ImageField(upload_to="static/image",null=True)
    title = models.CharField(max_length=255,default="title")
    company = models.CharField(max_length=255,default="company")
    skills = models.CharField(max_length=255,default="skill")
    location = models.CharField(max_length=50,default="Dehra")
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Projects(models.Model):
    image = models.ImageField(upload_to="static/image",null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    heading = models.CharField(max_length=255,default="heading")
    tools = models.CharField(max_length=200,default="tools")
    front = models.CharField(max_length=255,default="HTML")
    back = models.CharField(max_length=255,default="Python")
    database = models.CharField(max_length=200,default="MYSQL")
    image1 = models.ImageField(upload_to="static/image",null=True)
    description1 = models.TextField()
    image2 = models.ImageField(upload_to="static/image")
    description2 = models.TextField()
    profile = models.ImageField(upload_to="static/image")
    profile_description = models.TextField()
    product = models.ImageField(upload_to="static/image")
    product_description = models.TextField()
    product_detail = models.ImageField(upload_to="static/image")
    product_detail_description = models.TextField()
    cart = models.ImageField(upload_to="static/image",null=True)
    cart_description = models.TextField()
    wishlist = models.ImageField(upload_to="static/image",null=True)
    wishlist_description = models.TextField()
    duration = models.CharField(max_length=100)
    url = models.URLField(max_length=255,null=True)

    def __str__(self):
        return self.title


class image(models.Model):
    image1 = models.ImageField(upload_to="static/image")
