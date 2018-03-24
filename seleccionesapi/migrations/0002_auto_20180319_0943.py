# Generated by Django 2.0.3 on 2018-03-19 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seleccionesapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goles_local', models.IntegerField()),
                ('goles_visitante', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='seleccion',
            name='probabilidad',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=0),
        ),
        migrations.AddField(
            model_name='partido',
            name='seleccion_local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_fk', to='seleccionesapi.Seleccion'),
        ),
        migrations.AddField(
            model_name='partido',
            name='seleccion_visitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitante_fk', to='seleccionesapi.Seleccion'),
        ),
    ]
