from django.db import models

# Create your models here.
class users(models.Model):
    id = models.IntegerField(unique = True, primary_key = True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank = True)
    role  =models.CharField(max_length=255, null = True, blank = True)

    class Meta:
        verbose_name_plural = "Users DB"

    def __str__(self):
        return self.name
