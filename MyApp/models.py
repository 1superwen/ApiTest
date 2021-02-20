from django.db import models

# Create your models here.


class DB_tucao(models.Model):
    user = models.CharField(max_length=30, null=True)  # 吐槽人名字
    text = models.CharField(max_length=1000, null=True)   # 吐槽内容
    ctime = models.DateTimeField(auto_now=True)  # 创建时间

    def __str__(self):
        return self.text+str(self.ctime)
