# Generated by Django 3.0.4 on 2020-03-26 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('ticket_system', '0005_auto_20200326_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerips',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Buyer'),
        ),
        migrations.AlterField(
            model_name='place',
            name='in_basket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.Basket'),
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
    ]