# Generated by Django 4.1 on 2022-09-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='expired_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]