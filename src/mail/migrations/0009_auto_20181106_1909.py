# Generated by Django 2.1.3 on 2018-11-06 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0008_auto_20181023_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smtprelay',
            options={'ordering': ('ip_address', 'hostname'), 'verbose_name': 'smtp relay', 'verbose_name_plural': 'smtp relays'},
        ),
    ]
