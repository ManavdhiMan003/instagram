# Generated by Django 3.1.4 on 2020-12-30 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='name',
        ),
    ]