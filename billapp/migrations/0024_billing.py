# Generated by Django 4.2.1 on 2023-05-12 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0023_alter_partper_bdis_alter_partper_bkad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('no_of_product', models.IntegerField()),
                ('value', models.CharField(max_length=100)),
                ('rate_per_piece', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
            ],
        ),
    ]