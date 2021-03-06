# Generated by Django 3.2.4 on 2021-06-29 12:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('prioroty', models.CharField(choices=[('bg-danger', 'danger'), ('bg-warning', 'warning'), ('bg-info', 'info'), ('bg-success', 'success')], max_length=50, verbose_name='Prioroty')),
                ('star', models.BooleanField(default=False, verbose_name='Star/Unstar')),
                ('image', models.ImageField(upload_to='todo_poster/', verbose_name="Rasim qo'shish")),
            ],
        ),
    ]
