# Generated by Django 4.0.2 on 2022-02-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, db_index=True, max_length=16, null=True)),
                ('category', models.CharField(db_index=True, max_length=64)),
                ('url', models.URLField(blank=True, null=True)),
                ('error', models.TextField(max_length=256)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'error',
                'verbose_name_plural': 'errors',
                'db_table': 'logs',
            },
        ),
    ]
