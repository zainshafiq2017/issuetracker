# Generated by Django 2.0.2 on 2018-03-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20180310_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
