# Generated by Django 3.1.2 on 2020-10-14 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_posting', '0002_auto_20201014_0643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]