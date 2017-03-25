# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealpic', '0003_auto_20170324_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='zealicon',
            name='image2',
            field=models.ImageField(null=True, upload_to=b'images/'),
        ),
        migrations.AddField(
            model_name='zealicon',
            name='image3',
            field=models.ImageField(null=True, upload_to=b'images/'),
        ),
        migrations.AddField(
            model_name='zealicon',
            name='image4',
            field=models.ImageField(null=True, upload_to=b'images/'),
        ),
    ]
