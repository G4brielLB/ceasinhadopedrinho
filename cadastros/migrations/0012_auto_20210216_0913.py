# Generated by Django 3.1.6 on 2021-02-16 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0011_auto_20210216_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campo',
            old_name='logado',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='campo',
        ),
    ]
