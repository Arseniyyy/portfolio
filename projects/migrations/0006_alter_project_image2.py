# Generated by Django 3.2.6 on 2021-09-04 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]