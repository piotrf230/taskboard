# Generated by Django 4.2 on 2023-04-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0003_alter_task_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(default='', verbose_name=512),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default=('new', 'New'), verbose_name=20),
        ),
    ]
