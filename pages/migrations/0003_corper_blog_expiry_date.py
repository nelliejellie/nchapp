# Generated by Django 3.1.3 on 2021-04-22 03:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210420_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='corper_blog',
            name='expiry_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]