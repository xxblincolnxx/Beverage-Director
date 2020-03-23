# Generated by Django 3.0.4 on 2020-03-23 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bevdir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiscIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost_per_unit', models.IntegerField(default=0)),
                ('notes', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Spirit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(choices=[('Hookers house Bourbon', 'Hookers house Bourbon'), ('Jose Cuervo Reserva de Familia', 'Jose Cuervo Reserva de Familia'), ('Beefeater', 'Beefeater'), ('The Aperican Vodka', 'The Aperican Vodka'), ("Hatfield & McCoy The Devil's Fire Moonshine", "Hatfield & McCoy The Devil's Fire Moonshine"), ('Cragganmore Distillers Edition 12Y', 'Cragganmore Distillers Edition 12Y')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='cocktail',
            name='target_profit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(blank=True, default=0, null=True)),
                ('spirits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='bevdir.Spirit')),
            ],
        ),
    ]
