# Generated by Django 4.0.6 on 2022-07-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PublicacionAdmin', '0003_publicaciones_admins_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones_admins',
            name='titulo',
            field=models.TextField(default='Publicacion-10', max_length=60),
        ),
    ]