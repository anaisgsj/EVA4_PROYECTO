# Generated by Django 5.1.3 on 2024-11-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Título del proyecto', max_length=100)),
                ('ruts', models.JSONField(default=list, help_text="Lista de RUTs de los integrantes. Ej: ['12345678-9', '98765432-1']")),
                ('nombres', models.JSONField(default=list, help_text="Lista de nombres de los integrantes. Ej: ['Juan Pérez', 'María González']")),
            ],
        ),
    ]
