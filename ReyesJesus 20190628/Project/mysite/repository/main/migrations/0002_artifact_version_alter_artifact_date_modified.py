# Generated by Django 4.2 on 2023-04-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='version',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='date_modified',
            field=models.DateTimeField(),
        ),
    ]