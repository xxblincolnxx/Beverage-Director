# Generated by Django 3.0.4 on 2020-03-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bevdir', '0011_mystock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shot',
            name='volume',
            field=models.FloatField(default=0),
        ),
    ]
