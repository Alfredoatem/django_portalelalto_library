# Generated by Django 2.2.6 on 2020-08-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortalElAltoApp', '0002_snippet_font_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
