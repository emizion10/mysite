# Generated by Django 2.1 on 2018-11-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_ordercreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercreated',
            name='message',
            field=models.CharField(default='hi', max_length=200),
            preserve_default=False,
        ),
    ]