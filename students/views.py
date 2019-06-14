from .models import Questions
from django.shortcuts import render

def index(request):
    context={"Welcome":"Student Page"}
    return render(request,"students/index.html",context)

def student(request):
    context={"Wel":"Stud"}
    return render(request,"students/Student.html",context)

def cse_questions(request):
    questions=Questions.objects.all()
    return render(request,'students/cse ques.html',{'questions':questions})

def civil_questions(request):
    questions=Questions.objects.all()
    return render(request,'students/civil ques.html',{'questions':questions})

def electronics_questions(request):
    questions=Questions.objects.all()
    return render(request,'students/electronics ques.html',{'questions':questions})
