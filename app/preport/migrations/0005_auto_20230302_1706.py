# Generated by Django 3.2.16 on 2023-03-02 17:06

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('preport', '0004_db_attackflow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_risk_management',
            name='current_control',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management',
            name='impact_component',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management',
            name='reference',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management',
            name='risk_treatment_plan',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management',
            name='target_date',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management',
            name='threat',
            field=martor.models.MartorField(blank=True),
        ),
        migrations.AlterField(
            model_name='db_risk_management',
            name='vulnerability',
            field=martor.models.MartorField(blank=True),
        ),
    ]
