# Generated by Django 3.1.3 on 2021-04-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillhub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisan',
            name='categories',
            field=models.CharField(choices=[('not selected', 'not selected'), ('Carpenter', 'Carpenter'), ('Electrician', 'Electrician'), ('Realtor', 'Realtor'), ('Software-developer', 'Software-developer'), ('Personal-Shopper', 'Personal-Shopper'), ('beautician', 'beautician'), ('Hair-dresser', 'Hair-dresser'), ('Barber', 'Barber'), ('Fashion-designer', 'Fashion-designer'), ('Painter', 'Painter'), ('Photographer', 'Photographer'), ('Baker', 'Baker')], default='not selected', max_length=30),
        ),
    ]