# Generated by Django 3.0.5 on 2020-04-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
