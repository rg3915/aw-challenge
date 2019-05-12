from django.urls import path
from myproject.core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name="index"),
    path('repo/', v.repo_list, name="repo_list"),
]
