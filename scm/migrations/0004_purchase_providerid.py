# Generated by Django 4.0.2 on 2022-02-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scm', '0003_purchaseitem_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='providerid',
            field=models.CharField(default='na', max_length=100),
        ),
    ]
