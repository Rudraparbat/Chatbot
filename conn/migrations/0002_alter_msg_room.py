# Generated by Django 5.0.7 on 2024-07-10 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='conn.chatroom'),
        ),
    ]
