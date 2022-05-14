# Generated by Django 4.0.4 on 2022-05-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.tags'),
        ),
    ]
