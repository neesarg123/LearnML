# Generated by Django 3.0.7 on 2021-06-22 23:07

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0004_auto_20210622_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]