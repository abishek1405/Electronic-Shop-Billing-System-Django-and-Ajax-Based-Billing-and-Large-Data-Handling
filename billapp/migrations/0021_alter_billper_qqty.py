# Generated by Django 4.2.1 on 2023-05-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0020_alter_billper_dakad_alter_billper_dedis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billper',
            name='qqty',
            field=models.CharField(max_length=1500),
        ),
    ]