# Generated by Django 3.1.4 on 2021-01-01 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0002_remove_posts_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='name',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
