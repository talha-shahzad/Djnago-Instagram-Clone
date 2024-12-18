# Generated by Django 5.1 on 2024-08-23 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('story_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='story_pic/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='liked_stories', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
