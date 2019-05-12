import json
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


def repo_add(request):
    if request.method == 'POST':
        Repo.objects.all().delete()
        response = request.POST
        items = json.loads(response['item'])
        aux = []
        for item in items:
            obj = Repo(
                slug=item['id'],
                name=item['name'],
                full_name=item['full_name'],
                html_url=item['html_url'],
                stargazers_count=item['stargazers_count'],
            )
            aux.append(obj)
        Repo.objects.bulk_create(aux)
        repos = Repo.objects.all()
        data = [item.to_dict_json() for item in repos]
        return JsonResponse({'data': data})
