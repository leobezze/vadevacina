# Generated by Django 2.0.4 on 2019-08-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacina', models.CharField(max_length=255, verbose_name='Nome da Vacina')),
                ('lote', models.CharField(max_length=255, verbose_name='Lote')),
                ('resonsavel', models.CharField(max_length=255, verbose_name='resonsavel')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
            ],
        ),
    ]
