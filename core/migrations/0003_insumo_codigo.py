# Generated by Django 3.0.7 on 2020-06-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_insumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumo',
            name='codigo',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
