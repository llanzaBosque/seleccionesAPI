# Generated by Django 2.0.4 on 2018-04-28 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seleccionesapi', '0003_auto_20180331_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='seleccion_ganadora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ganadora_fk', to='seleccionesapi.Seleccion'),
        ),
    ]
