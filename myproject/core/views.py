from django.shortcuts import render


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def repo_list(request):
    template_name = 'core/repos_list.html'
    return render(request, template_name)
