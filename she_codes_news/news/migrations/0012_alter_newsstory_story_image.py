# Generated by Django 4.2.2 on 2023-12-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_newsstory_story_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='story_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploadImgs'),
        ),
    ]
