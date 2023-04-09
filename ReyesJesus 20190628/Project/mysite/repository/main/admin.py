from django.contrib import admin
from .models import Artifact

# Register your models here.

class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'level', 'version', 'date_modified')
    search_fields = ['name']
    list_filter = ['level', 'version']


admin.site.register(Artifact, ArtifactAdmin)
