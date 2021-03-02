# -*- coding: gbk -*-
from django.db import models
from statuscontroller.models import Projects


# Create your models here.
class Package(models.Model):
    target_project = models.ForeignKey(Projects, verbose_name="��Ӧ��Ŀ", on_delete=models.CASCADE)
    full_name = models.CharField("��ȫ��", max_length=50, default='')
    version = models.CharField("�汾��", max_length=50, default='')
    test_tool = models.CharField("���Թ���", max_length=50, default='')
    language = models.CharField("����", max_length=10, default='')
    description = models.TextField("������", default='')
    start_time = models.DateTimeField('��ʼʱ��', auto_now=True)
    time = models.DateTimeField('����ʱ��', auto_now=True)
    end_time = models.DateTimeField('����ʱ��', auto_now=True)
    analysis_status = models.IntegerField('����״̬', choices=((1, 'δ��ʼ'), (2, '���ڷ���'), (3, '�����')))
    result_description = models.TextField('����ļ�����', default='')

    def toDict(self):
        all_fields = dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

        choices = ((1, 'δ��ʼ'), (2, '���ڷ���'), (3, '�����'))
        for i in choices:
            if int(all_fields['analysis_status']) == i[0]:
                all_fields['analysis_status'] = i[1]
                break

        all_fields.pop('id')
        all_fields['target_project'] = self.target_project.name

        return all_fields
