from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Package


# Create your views here.
@csrf_exempt
def packageinfo(request, args):
    try:
        if request.method == 'GET':
            all_packages = Package.objects.all()

            path = request.path_info
            project_id = int(path[path.find('-') + 1:])

            data_info = []
            for package in all_packages:
                if package.target_project.id == project_id:
                    data_info.append(package.toDict())

            return render(request, 'package.html', {'data_info': data_info})

        elif request.method == 'POST':
            pass
    except Exception as e:
        print(e.args)
