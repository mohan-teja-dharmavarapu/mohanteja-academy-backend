# Generated by Django 5.0.2 on 2024-02-25 09:03

import django.db.models.deletion
import wagtail.fields
import wagtail.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0004_unit_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='chapter_belongs',
            new_name='chapter',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='artical',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='body',
        ),
        migrations.AddField(
            model_name='chapter',
            name='chapter_description',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='noof_topics',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='unit_name',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_description',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_number', models.IntegerField(blank=True, null=True)),
                ('topic_name', models.CharField(blank=True, null=True)),
                ('topic_description', wagtail.fields.RichTextField(blank=True, null=True)),
                ('topic_article', wagtail.fields.RichTextField(blank=True, null=True)),
                ('topic_video', models.FileField(blank=True, null=True, upload_to='')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maths.unit')),
            ],
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_number', models.IntegerField(blank=True, null=True)),
                ('problem_name', models.CharField(blank=True, null=True)),
                ('problem_question', wagtail.fields.RichTextField(blank=True, null=True)),
                ('problem_answer', wagtail.fields.RichTextField(blank=True, null=True)),
                ('problem_source', wagtail.fields.RichTextField(blank=True, null=True)),
                ('problem_article', wagtail.fields.RichTextField(blank=True, null=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maths.topic')),
            ],
        ),
    ]