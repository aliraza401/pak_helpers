# Generated by Django 3.0.5 on 2020-04-05 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200405_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='is_frequesnt',
            new_name='is_frequent',
        ),
    ]