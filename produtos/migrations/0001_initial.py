# Generated by Django 4.1.7 on 2023-03-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('unidade', models.IntegerField(verbose_name='Unidades vendidas')),
                ('em_estoque', models.CharField(max_length=8, verbose_name='Em estoque')),
                ('date', models.DateField(verbose_name='Data')),
            ],
        ),
    ]
