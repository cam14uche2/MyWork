# Generated by Django 4.1 on 2023-01-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storehuz', '0003_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]