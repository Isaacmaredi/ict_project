# Generated by Django 4.0.6 on 2022-07-12 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middlename', models.CharField(blank=True, max_length=200, null=True)),
                ('full_name', models.CharField(blank=True, editable=False, max_length=250, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('unit', models.CharField(max_length=200, verbose_name='ICT Unit')),
                ('position', models.CharField(max_length=200, verbose_name='Designation')),
                ('office_ext', models.CharField(max_length=100, verbose_name='Extension No.')),
                ('mobile', models.CharField(max_length=50, verbose_name='Mobile Number')),
                ('speed_dial', models.CharField(blank=True, max_length=50, null=True, verbose_name='Speed Dial')),
                ('photo', models.ImageField(default='default2.png', upload_to=profiles.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
