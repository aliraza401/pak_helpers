# Generated by Django 3.0.4 on 2020-03-30 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0007_auto_20200330_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='age',
            field=models.SmallIntegerField(null=True),
        ),
    ]
