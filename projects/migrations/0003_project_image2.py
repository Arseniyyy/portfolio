# Generated by Django 3.2.6 on 2021-09-03 04:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_some_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
