# Generated by Django 3.0.5 on 2020-04-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]