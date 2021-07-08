# Generated by Django 3.0.7 on 2021-07-07 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('explore', '0002_auto_20210706_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='helpfuls',
            field=models.ManyToManyField(blank=True, default=None, related_name='helpfuls', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Helpful',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Helpful', 'Helpful'), ('Unhelpful', 'Unhelpful')], max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]