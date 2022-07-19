# Generated by Django 4.0.5 on 2022-07-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
