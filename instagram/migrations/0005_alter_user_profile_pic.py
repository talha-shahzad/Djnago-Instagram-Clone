# Generated by Django 5.0.7 on 2024-08-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/default.png', upload_to='profile_pic/'),
        ),
    ]
