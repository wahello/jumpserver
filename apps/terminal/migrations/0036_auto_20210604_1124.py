# Generated by Django 3.1.6 on 2021-06-04 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0035_auto_20210517_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replaystorage',
            name='type',
            field=models.CharField(choices=[('null', 'Null'), ('server', 'Server'), ('s3', 'S3'), ('ceph', 'Ceph'), ('swift', 'Swift'), ('oss', 'OSS'), ('azure', 'Azure'), ('obs', 'OBS')], default='server', max_length=16, verbose_name='Type'),
        ),
    ]
