# Generated by Django 3.1.2 on 2020-11-28 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_size_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='season',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
