# Generated by Django 2.1.7 on 2019-04-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0003_governmentschemes_scheme_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='governmentschemes',
            name='scheme_name_hindi',
            field=models.CharField(default='', max_length=100),
        ),
    ]
