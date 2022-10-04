# Generated by Django 4.1 on 2022-08-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0005_alter_category_options_alter_job_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('full time', 'full time'), ('part time', 'part time')], default='full time', max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='workmode',
            field=models.CharField(choices=[('on-site', 'on-site'), ('remote', 'remote'), ('hybrid', 'hybrid')], default='on-site', max_length=30),
        ),
    ]