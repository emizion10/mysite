# Generated by Django 2.1 on 2018-11-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20181123_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='ownersofmenu', to='pages.student'),
        ),
    ]
