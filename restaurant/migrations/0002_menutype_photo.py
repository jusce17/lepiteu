# Generated by Django 3.0.5 on 2020-04-29 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutype',
            name='photo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]