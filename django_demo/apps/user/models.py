from django.db import models

from django_demo.utils.base_model import BaseModel


class UserInfo(BaseModel):
    class Meta:
        db_table = "userinfo"
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64,null=False,unique=True)
    pwd = models.CharField(max_length=128,null=False)
    email = models.CharField(max_length=128, null=False,unique=True)
    is_enabled = models.IntegerField(default=1,null=False)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()