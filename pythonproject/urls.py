from django.contrib import admin
from django.urls import include
from django.conf.urls import url

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^home/',include('students.url')),
    url(r'^accounts/', include('accounts.url')),
]

