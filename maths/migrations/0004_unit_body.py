# Generated by Django 5.0.2 on 2024-02-25 04:24

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0003_chapter_unit_delete_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]