# Generated by Django 3.0.4 on 2020-04-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_system', '0008_remove_place_reservation_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerips',
            name='time_logged',
            field=models.DateTimeField(null=True),
        ),
    ]