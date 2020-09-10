# Generated by Django 2.2.6 on 2020-08-20 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ContenidoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manifestacione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=700)),
                ('imagen1', models.ImageField(upload_to='turismo')),
                ('imagen2', models.ImageField(upload_to='turismo')),
                ('audio1', models.FileField(upload_to='turismo')),
                ('traducido', models.CharField(max_length=700)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='historia',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalhistoria',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='HistoricalManifestacione',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=700)),
                ('imagen1', models.TextField(max_length=100)),
                ('imagen2', models.TextField(max_length=100)),
                ('audio1', models.TextField(max_length=100)),
                ('traducido', models.CharField(max_length=700)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical manifestacione',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
