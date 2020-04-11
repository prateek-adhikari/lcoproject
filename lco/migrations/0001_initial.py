# Generated by Django 2.1 on 2020-04-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frequentlyaskquest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Moments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('our_story', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_num', models.IntegerField()),
                ('player_image', models.ImageField(upload_to='')),
                ('player_name', models.CharField(max_length=50)),
                ('player_pos', models.CharField(max_length=25)),
                ('player_height_f', models.IntegerField()),
                ('player_height_i', models.IntegerField()),
                ('player_weight', models.IntegerField()),
            ],
        ),
    ]