# Generated by Django 4.1 on 2023-01-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storehuz', '0002_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click to Read More', max_length=250),
        ),
    ]