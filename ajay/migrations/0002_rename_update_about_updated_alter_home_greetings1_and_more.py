# Generated by Django 4.1.2 on 2022-10-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='update',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings2',
            field=models.CharField(max_length=10),
        ),
    ]
