# Generated by Django 2.1.7 on 2019-03-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190319_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='customer_email',
            field=models.EmailField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='customer_no',
            field=models.IntegerField(default='0'),
        ),
    ]