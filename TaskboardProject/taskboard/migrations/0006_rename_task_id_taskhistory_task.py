# Generated by Django 4.2 on 2023-04-27 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0005_taskhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskhistory',
            old_name='task_id',
            new_name='task',
        ),
    ]