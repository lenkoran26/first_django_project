# Generated by Django 5.0.1 on 2024-01-16 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_created_date_alter_post_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
