# Generated by Django 2.0.1 on 2018-01-27 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipacionPolla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField()),
                ('eq_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_local', to='polla.Equipo')),
                ('eq_visita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_visita', to='polla.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Polla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.PositiveIntegerField()),
                ('participacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polla.ParticipacionPolla')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polla.Partido')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('tipo', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='participacionpolla',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polla.Usuario'),
        ),
    ]
