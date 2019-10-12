from django.db import models
from datetime import date

# Create your models here.
 
class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False) #todo: auto_now=True
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class User(models.Model):
    user_name=models.TextField(max_length=100,blank=False,unique=True)
    first_name=models.TextField(max_length=100,blank=False)
    last_name=models.TextField(max_length=100,blank=False)
    dob=models.DateField(default=date.today,blank=False)
    email_id=models.EmailField(max_length=70,blank=False,unique= True)

    def __str__(self):
        return self.user_name

class Channel(models.Model):
    channel_name=models.TextField(max_length=100,unique=True)
    videos=models.ForeignKey(Video,on_delete=models.DO_NOTHING,)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.channel_name

    

