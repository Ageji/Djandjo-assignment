# Generated by Django 2.2.6 on 2020-05-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0002_auto_20200522_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
