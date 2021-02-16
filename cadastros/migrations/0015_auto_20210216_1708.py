# Generated by Django 3.1.6 on 2021-02-16 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0014_ceasamodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verdura',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='verdura',
            name='data',
            field=models.DateField(default=datetime.date(2021, 2, 16)),
        ),
    ]