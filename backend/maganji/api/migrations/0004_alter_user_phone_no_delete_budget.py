# Generated by Django 5.2 on 2025-04-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
    ]
