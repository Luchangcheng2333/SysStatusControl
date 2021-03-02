# -*- coding: gbk -*-
from django import forms


class operationsForm(forms.Form):
    operation = forms.ChoiceField(choices=[(1, '添加'), (2, '删除')])
