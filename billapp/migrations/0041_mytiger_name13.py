# Generated by Django 4.2.1 on 2023-05-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0040_mytiger_name12'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytiger',
            name='name13',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]