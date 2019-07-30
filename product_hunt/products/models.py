from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes = models.IntegerField(default=1)
    url = models.TextField()
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title;

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

