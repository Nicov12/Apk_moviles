# Generated by Django 4.0.4 on 2022-05-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Becas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('porcentaje', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=100)),
                ('universidad', models.CharField(max_length=100)),
                ('requerimiento', models.CharField(max_length=500)),
            ],
        ),
    ]