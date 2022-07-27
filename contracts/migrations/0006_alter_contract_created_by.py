# Generated by Django 4.0.6 on 2022-07-20 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0005_alter_contract_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
