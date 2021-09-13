from django.shortcuts import render

from .models import Project


def projects_index(request):
    projects = Project.objects.all()
    for project in projects:
        print(project.image.url)

    context = {
        'projects': projects
    }

    return render(request, 'app/about.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)
