# Generated by Django 4.2.7 on 2023-12-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
    ]
