# Generated by Django 3.0.5 on 2020-04-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_auto_20200406_0506'),
        ('helper', '0017_auto_20200404_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='helper',
            name='contact_number',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='helper',
            name='profile_picture',
            field=models.ImageField(blank=True, default='helper_img/def_img.png', null=True, upload_to='helper_img'),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
    ]