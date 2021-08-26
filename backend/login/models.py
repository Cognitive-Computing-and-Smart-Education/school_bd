from django.db import models


# Create your models here.

class Group(models.Model):
    class Meta:
        verbose_name = "用户组"
        verbose_name_plural = "用户组"

    groupname = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.groupname


class User(models.Model):
    gender = (('male', "男"), ('female', '女'))  # 设置可选字段，性别

    id = models.IntegerField(primary_key=True, auto_created=True, default=1)
    name = models.CharField(max_length=16, unique=True, default='')
    password = models.CharField(max_length=16, unique=True, default='')
    sex = models.CharField(max_length=32, choices=gender, default='男')
    users = models.ForeignKey(Group, default='', validators='用户组')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
