# -*- coding: gbk -*-
from django import forms


class operationsForm(forms.Form):
    operation = forms.ChoiceField(choices=[(1, '���'), (2, 'ɾ��')])
