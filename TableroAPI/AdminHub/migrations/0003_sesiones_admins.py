# Generated by Django 4.0.6 on 2022-07-15 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminHub', '0002_alter_admins_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sesiones_Admins',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_sesion', models.DateTimeField()),
                ('cierre_sesion', models.DateTimeField()),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminHub.admins')),
            ],
        ),
    ]