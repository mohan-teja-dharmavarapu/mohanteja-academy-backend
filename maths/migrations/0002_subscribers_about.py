# Generated by Django 5.0.2 on 2024-02-25 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]