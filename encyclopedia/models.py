from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    imageUrl = models.CharField(max_length=1000)
    Completed = models.CharField(max_length=30 ,null=True)
    NameFor = models.CharField(max_length=50, null=True)
    Architect = models.CharField(max_length=50, null=True)
    Style = models.CharField(max_length=50, null=True)
    Materials = models.CharField(max_length=50, null=True)
    Location = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=500, null=True)
    Phone = models.CharField(max_length=20, null=True)
    isActive = models.BooleanField(default=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True, related_name="userComment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingComment")
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author} comment one {self.listing}"
    