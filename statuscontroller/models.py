# -*- coding: gbk -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Projects(models.Model):
    name = models.CharField('��Ŀȫ��', max_length=100, default='')
    owner = models.ForeignKey(User, verbose_name='������', on_delete=models.CASCADE)
    host_id = models.CharField('����ID', max_length=100, default='')
    host_ip = models.GenericIPAddressField('����IP��ַ', default='0.0.0.0')
    OS = models.CharField('����ϵͳ', max_length=50, default='')
    description = models.TextField('��Ŀ����', default='')
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

        return all_fields
