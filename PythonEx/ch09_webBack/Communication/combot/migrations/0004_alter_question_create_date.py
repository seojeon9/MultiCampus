# Generated by Django 4.1 on 2022-08-10 07:50

import combot.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combot', '0003_alter_question_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(default=combot.models.default_time),
        ),
    ]
