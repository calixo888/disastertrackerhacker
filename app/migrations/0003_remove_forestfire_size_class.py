# Generated by Django 3.0.5 on 2020-04-11 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_forestfire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forestfire',
            name='size_class',
        ),
    ]
