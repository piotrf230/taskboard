# Generated by Django 4.2 on 2023-04-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0002_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[(0, 'New'), (1, 'In Progress'), (2, 'Done')], default=(0, 'New'), verbose_name=20),
        ),
    ]