# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('dayday', '0002_auto_20180104_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('cgoods', models.ForeignKey(to='goods.GoodsInfo')),
                ('cuser', models.ForeignKey(to='dayday.UserInfo')),
            ],
        ),
    ]
