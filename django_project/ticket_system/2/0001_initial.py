# Generated by Django 3.0.3 on 2020-03-24 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('house_number', models.CharField(max_length=50)),
                ('flat_number', models.CharField(max_length=50)),
                ('post_code', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.IntegerField()),
                ('sector', models.CharField(max_length=2)),
                ('row', models.IntegerField(verbose_name=8)),
                ('number', models.IntegerField(verbose_name=100)),
                ('status', models.CharField(choices=[('AV', 'Available'), ('DI', 'Disabled'), ('SE', 'Selected'), ('RE', 'Reserved')], default='AV', max_length=2)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_value', models.IntegerField()),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_system.Place')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=50)),
                ('basket', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ticket_system.Basket')),
                ('delivery_data', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='ticket_system.DeliveryData')),
            ],
        ),
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_system.Place')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_system.User')),
            ],
        ),
    ]