# Generated by Django 3.2.16 on 2023-03-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preport', '0006_auto_20230302_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_risk_management',
            name='target_date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='db_risk_management_template',
            name='target_date',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
