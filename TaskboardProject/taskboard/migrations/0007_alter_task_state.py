# Generated by Django 4.2 on 2023-04-27 17:34

from django.db import migrations, models
import taskboard.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0006_rename_task_id_taskhistory_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], default=('new', 'New'), validators=[taskboard.validators.task_state_validator], verbose_name=20),
        ),
    ]
