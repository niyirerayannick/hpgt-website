# Generated by Django 4.1.7 on 2023-03-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famil',
            name='about_fam',
            field=models.TextField(default=''),
        ),
    ]