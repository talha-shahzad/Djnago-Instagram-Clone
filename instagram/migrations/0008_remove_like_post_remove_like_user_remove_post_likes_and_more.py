# Generated by Django 5.1 on 2024-08-23 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_remove_user_follower_user_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.RemoveField(
            model_name='story',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='story',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]
