# Generated by Django 4.0.4 on 2022-05-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comment'},
        ),
        migrations.AddField(
            model_name='comments',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]