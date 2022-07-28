# Generated by Django 4.0.6 on 2022-07-27 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='members', to='projects.team'),
        ),
    ]
