# Generated by Django 3.1.2 on 2020-10-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
