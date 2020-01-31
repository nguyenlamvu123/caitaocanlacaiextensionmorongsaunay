from django.db import models

class dictionary(models.Model):
    Eng = models.CharField(max_length=255)
    Viet = models.CharField(max_length=255)
    pronunciation = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "Engsssss"

    def __str__(self):
        return self.Eng
