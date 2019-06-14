from . import views
from django.conf.urls import url


app_name = "students"

urlpatterns = [
    url(r'^$', views.index, name='index'),
url(r'^cse_questions',views.cse_questions,name='cse_questions'),
url(r'^electronics_questions',views.electronics_questions,name='electronics_questions'),
url(r'^civil_questions',views.civil_questions,name='civil_questions'),
url(r'^stusection/', views.student, name='student'),


]