from django.contrib import admin
from .models import Student,Teacher,Questions,Reply

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Questions)
admin.site.register(Reply)