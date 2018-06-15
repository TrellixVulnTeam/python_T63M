# -*- utf-8 -*-
from django.db import models


class Person(models.Model):
    # 主键
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
