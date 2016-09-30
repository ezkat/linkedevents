# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-25 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_auto_20160819_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasource',
            name='api_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='datasource',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_system', to='events.Organization'),
        ),
        migrations.AlterField(
            model_name='event',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_event_data', to='events.DataSource'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_keyword_data', to='events.DataSource'),
        ),
        migrations.AlterField(
            model_name='keywordset',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_keywordset_data', to='events.DataSource'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_organization_data', to='events.DataSource'),
        ),
        migrations.AlterField(
            model_name='place',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_place_data', to='events.DataSource'),
        ),
    ]
