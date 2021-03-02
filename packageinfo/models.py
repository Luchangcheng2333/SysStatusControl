# -*- coding: gbk -*-
from django.db import models
from statuscontroller.models import Projects


# Create your models here.
class Package(models.Model):
    target_project = models.ForeignKey(Projects, verbose_name="对应项目", on_delete=models.CASCADE)
    full_name = models.CharField("包全名", max_length=50, default='')
    version = models.CharField("版本名", max_length=50, default='')
    test_tool = models.CharField("测试工具", max_length=50, default='')
    language = models.CharField("语言", max_length=10, default='')
    description = models.TextField("包描述", default='')
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

        all_fields.pop('id')
        all_fields['target_project'] = self.target_project.name

        return all_fields
