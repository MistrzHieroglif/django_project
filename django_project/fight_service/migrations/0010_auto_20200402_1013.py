# Generated by Django 3.0.4 on 2020-04-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fight_service', '0009_auto_20200402_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='image',
            field=models.FileField(blank=True, default='fighters/fighter.png', upload_to='fighters_img', verbose_name='Zdjęcie zawodnika'),
        ),
    ]