# Generated by Django 3.0.4 on 2020-04-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0015_auto_20200402_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='helper.Category'),
        ),
    ]
