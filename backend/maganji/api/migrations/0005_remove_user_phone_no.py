# Generated by Django 5.2 on 2025-04-07 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_phone_no_delete_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_no',
        ),
    ]
