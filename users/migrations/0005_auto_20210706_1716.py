# Generated by Django 3.0.7 on 2021-07-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210706_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_link',
            field=models.URLField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insta_link',
            field=models.URLField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin_link',
            field=models.URLField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_link',
            field=models.URLField(blank=True, default='#', max_length=100),
        ),
    ]
