# Generated by Django 4.0.4 on 2022-05-29 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0004_post_comment_status'),
        ('account', '0003_account_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archive_acc', to='account.account')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archive_post', to='posts.post')),
            ],
        ),
    ]
