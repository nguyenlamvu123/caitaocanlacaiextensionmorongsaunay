from django.db import models

#Create your models here.
class Idol(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField(blank=True)

    def __str__(self):
    #def __unicode__(self):
        return self.name

class Video(models.Model):
    idol = models.ForeignKey(Idol, on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
