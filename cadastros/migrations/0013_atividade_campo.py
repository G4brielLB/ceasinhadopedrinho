# Generated by Django 3.1.6 on 2021-02-16 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0012_auto_20210216_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='campo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='cadastros.campo'),
            preserve_default=False,
        ),
    ]
