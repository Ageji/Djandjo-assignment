# Generated by Django 2.2.6 on 2020-06-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0007_post_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkmask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_image', models.ImageField(upload_to='detected')),
            ],
        ),
    ]
