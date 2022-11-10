# from email.policy import default
from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
import datetime
from django.utils.html import format_html
# Create your models here.
# Category Model 
now = timezone.now()
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=55)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title
    def image_tag(self):
        return format_html("<img src='/media/{}'  style='max-height:100px;max-width:180px;border-radius:50%'  />".format(self.image))
# News Model 
class News(models.Model):
    date = models.DateField(("Date"), default=datetime.date.today)
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    brief = HTMLField()
    time = models.TimeField(default=now)
    url = models.CharField(max_length=55)
    image = models.ImageField(upload_to='news/')
    img2 = models.ImageField(upload_to='news/', default='default.png')
    img3 = models.ImageField(upload_to='news/', default='default.png')
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class SocialPage(models.Model):
    fb = models.CharField(max_length=1000)
    insta = models.CharField(max_length=1000)
    yt = models.CharField(max_length=1000)
    twt = models.CharField(max_length=1000)


