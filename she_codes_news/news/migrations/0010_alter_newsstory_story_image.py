# Generated by Django 4.2.2 on 2023-12-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_newsstory_story_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='story_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploadImgs/'),
        ),
    ]
