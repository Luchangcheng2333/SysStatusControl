# -*- coding: gbk -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Projects(models.Model):
    name = models.CharField('项目全名', max_length=100, default='')
    owner = models.ForeignKey(User, verbose_name='所有者', on_delete=models.CASCADE)
    host_id = models.CharField('主机ID', max_length=100, default='')
    host_ip = models.GenericIPAddressField('主机IP地址', default='0.0.0.0')
    OS = models.CharField('操作系统', max_length=50, default='')
    description = models.TextField('项目描述', default='')
    start_time = models.DateTimeField('开始时间', auto_now=True)
    time = models.DateTimeField('运行时长', auto_now=True)
    end_time = models.DateTimeField('结束时间', auto_now=True)
    analysis_status = models.IntegerField('分析状态', choices=((1, '未开始'), (2, '正在分析'), (3, '已完成')))
    result_description = models.TextField('结果文件介绍', default='')

    def toDict(self):
        all_fields = dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

        choices = ((1, '未开始'), (2, '正在分析'), (3, '已完成'))
        for i in choices:
            if int(all_fields['analysis_status']) == i[0]:
                all_fields['analysis_status'] = i[1]
                break

        return all_fields
