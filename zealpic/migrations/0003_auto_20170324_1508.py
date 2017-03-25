# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealpic', '0002_auto_20160402_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zealicon',
            name='image',
            field=models.ImageField(upload_to=b'images/'),
        ),
    ]
