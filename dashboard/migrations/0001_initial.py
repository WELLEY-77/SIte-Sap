# Generated by Django 4.1.7 on 2023-03-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Descrição')),
                ('stats', models.CharField(max_length=20, verbose_name='Estatos')),
                ('hour', models.IntegerField(verbose_name='Horas')),
            ],
        ),
    ]
