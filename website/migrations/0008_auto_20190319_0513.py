# Generated by Django 2.1.7 on 2019-03-19 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_email_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='date',
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='time',
        ),
        migrations.AddField(
            model_name='user_data',
            name='date_time',
            field=models.CharField(default='', max_length=200),
        ),
    ]
