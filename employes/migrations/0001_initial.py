# Generated by Django 4.1.3 on 2022-11-09 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('emp_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('emp_phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('emp_gender', models.CharField(max_length=255, verbose_name='Gender')),
                ('emp_marital', models.CharField(max_length=255, verbose_name='Marital')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]