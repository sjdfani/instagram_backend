# Generated by Django 4.0.4 on 2022-05-31 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_alter_account_last_login'),
        ('posts', '0004_post_comment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_acc', to='account.account')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_post', to='posts.post')),
            ],
        ),
    ]
