# Generated by Django 2.2.5 on 2021-02-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0002_auto_20210210_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.TextField(default='Hindi'),
            preserve_default=False,
        ),
    ]
