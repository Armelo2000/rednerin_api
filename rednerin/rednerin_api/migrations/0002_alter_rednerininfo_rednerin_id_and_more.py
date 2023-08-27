# Generated by Django 4.2.4 on 2023-08-20 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rednerin_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rednerininfo',
            name='rednerin_Id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='rednerin_api.rednerin'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='rednerinInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialnetwork', to='rednerin_api.rednerininfo'),
        ),
        migrations.AlterField(
            model_name='url',
            name='rednerinInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url', to='rednerin_api.rednerininfo'),
        ),
        migrations.AlterField(
            model_name='video',
            name='rednerinInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='rednerin_api.rednerininfo'),
        ),
    ]