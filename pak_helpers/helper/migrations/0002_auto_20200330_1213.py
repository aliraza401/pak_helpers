# Generated by Django 3.0.4 on 2020-03-30 12:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasker',
            new_name='Helper',
        ),
    ]
