# Generated by Django 4.2.1 on 2023-05-10 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0014_part_noqty_part_toqrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='billper',
            name='perp',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]