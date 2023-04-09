from django.db import models

# Create your models here.

level_choice = (('GI', 'Goals & Initiatives'),
                ('PS', 'Products & Services'),
                ('DI', 'Data & Information'),
                ('SA', 'Systems & Applications'),
                ('NI', 'Networks & Infrastructure'),
            )


class Artifact(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    date_modified = models.DateTimeField()
    level = models.CharField(max_length=10, choices=level_choice, default='GI')
    version = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
