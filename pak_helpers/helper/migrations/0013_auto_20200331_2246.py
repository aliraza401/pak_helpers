# Generated by Django 3.0.4 on 2020-03-31 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0012_auto_20200331_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='cnic',
            field=models.CharField(max_length=15),
        ),
    ]
