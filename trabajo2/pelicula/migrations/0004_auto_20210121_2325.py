# Generated by Django 3.1.2 on 2021-01-22 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0003_auto_20210121_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
