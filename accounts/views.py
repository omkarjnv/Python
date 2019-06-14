from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegistartionForm,CreateStudent,CreateTeacher
from students.models import Student,Teacher,Questions,Reply
from django.contrib.auth import login,logout

username = None
num= None
QNO = None
def setval(val):
    global username
    username = val


def signup(request):
    if request.method == 'POST':
        form = RegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:index')
    else:
        form=RegistartionForm()
    return render(request,'accounts/signup.html', {'form' : form})


def stu_details(request):
    if request.method == 'POST':
        if request.POST.get('usn')!=None and request.POST.get('name')!=None and request.POST.get('sem')!=None and request.POST.get(
                'dept')!=None:
            print("Hie")
            form = Student()
            form.USN = request.POST['usn']
            form.name = request.POST['name']
            form.sem = request.POST['sem']
            form.Dept = request.POST['dept']
            form.save()
            return redirect('accounts:signup')

    else:
        form= Student

    return render(request,'accounts/student_details.html')



def teach_details(request):
    if request.method == 'POST':
        if request.POST.get('eid')!=None and request.POST.get('name')!=None and request.POST.get('dept')!=None and request.POST.get(
                'contact')!=None:
            print("Hie")
            form = Teacher()
            form.EID = request.POST['eid']
            form.name = request.POST['name']
            form.Dept = request.POST['dept']
            form.Contact = request.POST['contact']
            form.save()
            return redirect('accounts:signup')

    else:
        form= Teacher
        return render(request, 'accounts/teacher_details.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            setval(user)
            return redirect('students:index')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def ques_list(request):
    quesobjs=Questions.objects.all()
    totalques=len(quesobjs)
    student=Student.objects.filter(name__exact=username)
    usn = Questions.objects.filter(name__exact=username)
    solutions = Reply.objects.all()
    number=len(usn)
    context = {'usn': usn, 'number': number ,'name':username,'solutions':solutions}
    if request.method == 'POST':
        if request.POST.get('question') != None:
            form=Questions()
            form.QNO=totalques+1
            form.QID=usn[0].QID
            form.name=username
            form.Dept=usn[0].Dept
            form.Text=request.POST['question']
            form.save()
            print("DATA SAVED")
            return redirect('accounts:ques_num')

    else:
        form=Questions()


    return render(request, 'students/Student.html', context)

def ques_num(request):
    quesobjs = Questions.objects.all()
    totalques = len(quesobjs)
    student = Student.objects.filter(name__exact=username)
    usn = Questions.objects.filter(name__exact=username)
    solutions = Reply.objects.all()
    number = len(usn)
    context = {'usn': usn, 'number': number, 'name': username, 'solutions': solutions}
    if request.method == 'POST':
        if request.POST.get('qno') != None:
            global QNO
            QNO=request.POST['qno']
            print(QNO)
            print("working")
            return redirect('accounts:replies')

    else:
        form = Questions()

    return render(request, 'students/Student - Copy.html', context)

def replies(request):
    solutions=Reply.objects.filter(RID__QNO=QNO)
    context={'solutions':solutions}
    if request.method == 'POST':
        print(QNO)
        if request.POST.get('reply')!=None:
            form=Reply()
            form.RID=QNO
            form.Text=request.POST['reply']
            form.name=username
            form.save()
            print("Reply saved")
    return render(request, 'students/Replies.html',context)


def logout_view(request):
    if request.method=='POST':
        logout(request)
        global username
        username=None
        return redirect('students:index')
