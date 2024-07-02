# Generated by Django 5.0.4 on 2024-06-30 02:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AulaVirtual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('curso', models.CharField(max_length=75)),
                ('estado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='EducacionGlobal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.BinaryField()),
                ('nombres_institucion', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('referencia_ubicacion', models.CharField(max_length=500)),
                ('estado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=75)),
                ('estado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Paralelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paralelo', models.CharField(max_length=75)),
                ('estado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='AulaVirtualEstudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_asistencia', models.FloatField()),
                ('estado', models.CharField(max_length=3)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.aulavirtual')),
            ],
        ),
        migrations.AddField(
            model_name='aulavirtual',
            name='id_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.curso'),
        ),
        migrations.CreateModel(
            name='ConfiguracionEducacionGlobal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_asistencia', models.IntegerField()),
                ('estado', models.CharField(max_length=3)),
                ('id_educacion_global', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.educacionglobal')),
            ],
        ),
        migrations.AddField(
            model_name='aulavirtual',
            name='id_educacion_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.educacionglobal'),
        ),
        migrations.AddField(
            model_name='aulavirtual',
            name='id_materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.materia'),
        ),
        migrations.AddField(
            model_name='aulavirtual',
            name='id_paralelos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.paralelo'),
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.BinaryField()),
                ('cedula', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=25)),
                ('pais_natal', models.CharField(max_length=100)),
                ('ciudad_natal', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=3)),
                ('id_perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.perfil')),
            ],
        ),
        migrations.AddField(
            model_name='aulavirtual',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrativa.usuarios'),
        ),
    ]
