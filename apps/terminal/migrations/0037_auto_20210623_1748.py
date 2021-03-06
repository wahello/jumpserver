# Generated by Django 3.1.6 on 2021-06-23 09:48

from django.db import migrations, models


def set_default_storage(apps, schema_editor):
    command_storage_model = apps.get_model("terminal", "CommandStorage")
    command_storage = command_storage_model.objects.filter(name='default', type='server').first()
    if command_storage:
        command_storage.is_default = True
        command_storage.save()
    replay_storage_model = apps.get_model("terminal", "ReplayStorage")
    replay_storage = replay_storage_model.objects.filter(name='default', type='server').first()
    if replay_storage:
        replay_storage.is_default = True
        replay_storage.save()


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0036_auto_20210604_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandstorage',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Default storage'),
        ),
        migrations.AddField(
            model_name='replaystorage',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Default storage'),
        ),
        migrations.RunPython(set_default_storage)
    ]
