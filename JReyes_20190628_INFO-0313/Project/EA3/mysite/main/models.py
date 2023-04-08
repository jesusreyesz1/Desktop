from django.db import models

# Create your models here.
class Artifact(models.Model):
    Art_name = models.CharField(max_length=100)
    date_Modified = models.DateField(auto_now_add=True)
    LEVEL_CHOICES = [
        ('Goal & Initiatives', 'GI'),
        ('Products & Service', 'PS'),
        ('Data & Information', 'DI'),
        ('Network & Infrastructure', 'NI'),

        ]
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    version = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.Art_name}{self.level}")
