# Generated by Django 3.2 on 2021-06-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_list_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='category',
        ),
        migrations.AddField(
            model_name='listing',
            name='branch',
            field=models.CharField(blank=True, choices=[('First-Year Engineering', 'First-Year Engineering'), ('Computer Engineering', 'Computer Engineering'), ('Information Technology', 'Information Technology'), ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Automobile Engineering', 'Automobile Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Master of Business Administration', 'Master of Business Administration')], max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='semester',
            field=models.CharField(blank=True, choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8')], max_length=100),
        ),
    ]
