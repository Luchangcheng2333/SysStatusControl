# -*- coding: gbk -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Projects
from .form import operationsForm


# Create your views here.


@csrf_exempt
def projectinfo(request):
    try:
        if request.method == 'GET':
            obj = operationsForm()
            projects_data = Projects.objects.all()

            data_info = []
            for project in projects_data:
                data_info.append(project.toDict())

            return render(request, 'project.html', {'data_info': data_info, 'obj': obj})
        elif request.method == 'POST':
            print("收到POST请求：")
            print(request.POST.get('selected_value'))
            return HttpResponse("成功收到消息")

    except Exception as e:
        return e.args

