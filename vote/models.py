from PIL import Image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import PROTECT, CASCADE, SET_NULL


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Candidate(models.Model):
    year = (('Y1S1', 'Y1S1'), ('Y1S2', 'Y1S2'), ('Y2S1', 'Y2S1'), ('Y2S2', 'Y2S2'), ('Y3S1', 'Y3S1'),
            ('Y3S2', 'Y3S2'), ('Y4S1', 'Y4S1'), ('Y4S2', 'Y4S2'))
    category=(('chairman','chairman'),('secretary','secretary'),('Entertainment','Entertainment'),('Treasurer','Treasurer'),('Academic','Academic'))
    course = (('m', 'M & I'), ('b', 'BPS'), ('m', 'MMPE'), ('b', 'BCOM'), ('i', 'I & C'))
    SEX = (('m', 'male'), ('f', 'Female'))
    FirstName = models.TextField()
    LastName = models.TextField()
    Gender = models.TextField(max_length=5, default='male', choices=SEX)
    Reg_No = models.CharField(max_length=20,primary_key=True)
    YearSem = models.CharField(max_length=4, choices=year)
    Course = models.CharField(max_length=50, choices=course)
    Category = models.CharField(max_length=50,choices=category)
    profilePic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.Reg_No + " " + self.Category
    def save(self):
        super().save()
        img=Image.open(self.profilePic.path)
        if img.height>300 and img.width > 300:
            cropped=(300,300)
            img.thumbnail(cropped)
            img.save(self.profilePic.path)


class Vote(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    chairman = models.CharField(max_length=50)
    secretary = models.CharField(max_length=50)
    Entertainment = models.CharField(max_length=50)
    Treasurer = models.CharField(max_length=50)
    Academic = models.CharField(max_length=50)

    def __str__(self):

        return 'Voted'