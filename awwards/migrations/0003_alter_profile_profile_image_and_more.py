# Generated by Django 4.0.3 on 2022-03-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0002_alter_profile_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profile.png', upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='projectposts',
            name='landing_page',
            field=models.ImageField(upload_to='image'),
        ),
    ]