# Generated by Django 2.1.7 on 2019-03-15 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_user_data_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='total_price',
        ),
    ]