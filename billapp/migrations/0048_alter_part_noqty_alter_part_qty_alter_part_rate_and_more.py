# Generated by Django 4.2.1 on 2023-05-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0047_alter_mytiger_name11_alter_mytiger_name12_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='noqty',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='part',
            name='qty',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='part',
            name='rate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='part',
            name='toqrate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='part',
            name='totalfee',
            field=models.CharField(max_length=100),
        ),
    ]