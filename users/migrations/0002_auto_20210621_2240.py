# Generated by Django 3.0.7 on 2021-06-22 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.svg', upload_to='profile_pics'),
        ),
    ]
