# Generated by Django 4.0.6 on 2022-07-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumno', '0004_delete_alumnos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_programa', models.TextField(max_length=60)),
                ('clave_programa', models.IntegerField(null=True)),
                ('plan', models.IntegerField(null=True)),
                ('expediente', models.IntegerField(null=True)),
                ('nombre', models.TextField(max_length=60)),
                ('status', models.TextField(max_length=20)),
                ('cred_pasante', models.IntegerField(null=True)),
                ('cred_aprob', models.IntegerField(null=True)),
                ('prom_kdxs', models.FloatField(null=True)),
                ('prom_periodo', models.FloatField(null=True)),
                ('mat_aprob', models.IntegerField(null=True)),
                ('materias_acreditadas', models.TextField(blank=True, max_length=255)),
                ('materias_segunda_inscr', models.TextField(blank=True, max_length=255)),
                ('materias_tercera_inscr', models.TextField(blank=True, max_length=255)),
                ('materias_reprobadas', models.TextField(blank=True, max_length=255)),
                ('materias_bajas_voluntarias', models.TextField(blank=True, max_length=255)),
                ('cred_inscr', models.IntegerField(null=True)),
                ('nivel_y_ciclo_ingles', models.TextField(max_length=10)),
                ('correo', models.TextField(max_length=25)),
                ('cred_cult', models.FloatField(null=True)),
                ('cred_dep', models.FloatField(null=True)),
                ('practica_profesional_estatus_y_ciclo', models.TextField(blank=True, max_length=20)),
                ('serviciosocialmateriaestatus_ciclo', models.TextField(blank=True, max_length=20)),
                ('estatusproyectoserviciosocial_cicloregistro', models.TextField(blank=True, max_length=20)),
                ('egel_testimonio', models.TextField(blank=True, max_length=60)),
                ('inscrito', models.BooleanField()),
            ],
        ),
    ]
