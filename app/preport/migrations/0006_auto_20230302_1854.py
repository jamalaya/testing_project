# Generated by Django 3.2.16 on 2023-03-02 18:54

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('preport', '0005_auto_20230302_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='current_control',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='impact_component',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='reference',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='risk_treatment_plan',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='target_date',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='threat',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='vulnerability',
            field=martor.models.MartorField(blank=True),
        ),
    ]
