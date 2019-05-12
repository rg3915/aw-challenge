from django.http import JsonResponse
from django.shortcuts import render
from .models import Repo


def index(request):
    template_name = 'core/index.html'
    return render(request, template_name)


def repo_list(request):
    template_name = 'core/repos_list.html'
    return render(request, template_name)


def repo_json(request):
    ''' Retorna um JSON dos repos. '''
    repos = Repo.objects.all()
    data = [item.to_dict_json() for item in repos]
    return JsonResponse({'data': data})
