# Generated by Django 4.0.4 on 2022-05-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
