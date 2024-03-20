from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'projects'
    number = 11
    context = {'page' : page, 'number':number, 'projects':projectsList}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
