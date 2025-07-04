# Generated by Django 5.2.3 on 2025-06-25 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='folder.folder'),
        ),
        migrations.AlterField(
            model_name='file',
            name='root_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_files', to='folder.folder'),
        ),
    ]
