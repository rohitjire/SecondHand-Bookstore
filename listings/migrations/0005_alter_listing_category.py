# Generated by Django 3.2 on 2021-06-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20210611_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('Books', 'Books'), ('Notes', 'Notes'), ('Stationary Tools', 'Stationary Tools')], max_length=100),
        ),
    ]
