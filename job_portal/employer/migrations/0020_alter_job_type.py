# Generated by Django 4.1 on 2022-09-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0019_alter_job_workmode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(default='Full time', max_length=30),
        ),
    ]