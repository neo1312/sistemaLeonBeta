# Generated by Django 4.0.2 on 2022-05-18 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_alter_saleitem_margen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(default='mostrador', null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.client')),
            ],
            options={
                'verbose_name': 'devolution',
                'verbose_name_plural': 'devolutions',
                'ordering': ['date_created'],
            },
        ),
    ]
