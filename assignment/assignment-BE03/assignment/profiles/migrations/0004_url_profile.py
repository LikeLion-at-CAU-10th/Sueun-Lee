# Generated by Django 4.0.2 on 2022-07-19 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_url_pup_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
