# Generated by Django 2.0.4 on 2019-08-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0002_vacina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacina',
            name='slug',
        ),
        migrations.AlterField(
            model_name='vacina',
            name='resonsavel',
            field=models.CharField(max_length=255, verbose_name='responsavel'),
        ),
    ]