# Generated by Django 4.1.6 on 2023-02-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230205_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costomusers',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
