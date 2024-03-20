from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
        {
            'id': '1',
            'title':"Ecommerece website",
            'description':'Fully functional ecommerece website'
        },
        {
            'id':'2',
            'title':"Portfolio website",
            'description':"This was a project where I"
        },
        {
            'id':'3',
            'title':"Social Network",
            'description':"Awosome open source project"
        },
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    print('projectObj:', projectObj)
    return render(request, 'projects/single-project.html', {'project': projectObj})
