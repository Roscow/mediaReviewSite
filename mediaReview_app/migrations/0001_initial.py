# Generated by Django 5.0 on 2023-12-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalisisDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('buenas', models.IntegerField()),
                ('malas', models.IntegerField()),
                ('neutra', models.IntegerField()),
                ('total', models.IntegerField()),
                ('data_scraping', models.IntegerField()),
            ],
            options={
                'db_table': 'analisis_diario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnalisisGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('buenas', models.IntegerField()),
                ('malas', models.IntegerField()),
                ('neutra', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'analisis_general',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contexto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'contexto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion_web', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'medio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedioDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'medio_diario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'noticia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('romano', models.CharField(max_length=10)),
                ('numero', models.IntegerField()),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
    ]
