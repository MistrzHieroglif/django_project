# Generated by Django 3.0.4 on 2020-04-06 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fight_service', '0011_auto_20200406_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='FightCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='fighters_img', verbose_name='Zdjęcie promujące pojedynek')),
                ('category', models.CharField(max_length=10, verbose_name='Kategoria wagowa')),
                ('main_event', models.BooleanField(default=False, verbose_name='Czy posiada pas mistrzowski?')),
                ('description', models.TextField(verbose_name='Opis')),
                ('priority', models.IntegerField(default=0, verbose_name='Priorytet')),
                ('fighter_left', models.CharField(max_length=50, verbose_name='Zawodnik z lewej')),
                ('fighter_right', models.CharField(max_length=50, verbose_name='Zawodnik z prawej')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Imie')),
                ('surname', models.CharField(max_length=20, verbose_name='Nazwisko')),
                ('role', models.CharField(max_length=30, verbose_name='Rola w zespole')),
                ('description', models.TextField(verbose_name='Opis')),
                ('priority', models.IntegerField(default=0, verbose_name='Priorytet')),
                ('image', models.FileField(blank=True, upload_to='team_img', verbose_name='Zdjęcie')),
                ('published', models.BooleanField(default=True, verbose_name='Czy opublikować na stronie?')),
            ],
        ),
        migrations.AlterField(
            model_name='fighter',
            name='image',
            field=models.FileField(blank=True, upload_to='fighters_img', verbose_name='Zdjęcie zawodnika'),
        ),
        migrations.CreateModel(
            name='TeamMemberLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nazwa')),
                ('url', models.CharField(max_length=200, verbose_name='Adres linku')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='links', to='fight_service.TeamMember')),
            ],
        ),
    ]
