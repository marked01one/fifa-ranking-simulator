# Generated by Django 4.1.5 on 2023-01-21 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confederation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('fifa_code', models.CharField(max_length=3)),
                ('flag_url', models.CharField(max_length=255)),
                ('confederation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.confederation')),
            ],
        ),
    ]
