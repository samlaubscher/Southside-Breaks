# Generated by Django 4.0.6 on 2022-07-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_mixes', '0003_alter_guestmix_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestmix',
            name='number',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
    ]
