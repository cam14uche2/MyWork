# Generated by Django 4.1 on 2023-01-28 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERAUTH', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]