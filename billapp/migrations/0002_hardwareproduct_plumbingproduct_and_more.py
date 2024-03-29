# Generated by Django 4.1.6 on 2023-05-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardwareProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('qty', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlumbingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('qty', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='productlist',
            new_name='ElectricProduct',
        ),
    ]
