# Generated by Django 2.0.4 on 2018-05-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seleccionesapi', '0004_auto_20180427_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuartos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pos', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'cuartos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pos', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'final',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_a',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_b',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_c',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_d',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_e',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_f',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_g',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo_h',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Octavos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pos', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'octavos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Podio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('pos', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'podio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semifinales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('pos', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'semifinales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tercerlugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pos', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tercerlugar',
                'managed': False,
            },
        ),
    ]
