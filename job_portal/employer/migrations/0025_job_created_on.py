# Generated by Django 4.1 on 2022-10-03 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0024_rename_locn_job_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]