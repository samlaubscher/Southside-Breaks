# Generated by Django 4.0.6 on 2022-07-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_mixes', '0005_alter_guestmix_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestmix',
            name='soundcloud_iframe_code',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]