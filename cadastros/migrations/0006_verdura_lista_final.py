# Generated by Django 3.1.6 on 2021-02-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_auto_20210213_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='verdura',
            name='lista_final',
            field=models.IntegerField(default=0, verbose_name='Verduras'),
            preserve_default=False,
        ),
    ]
