from . import views
from django.conf.urls import url

app_name = "accounts"

urlpatterns = [

    url(r'^teacher_signup/',views.teach_details,name="teacher_signup"),
    url(r'^student_signup/',views.stu_details,name="student_signup"),
    url(r'^signup/',views.signup,name="signup"),
    url(r'^login/', views.login_view, name="login"),
    url(r'^queslist/', views.ques_list, name="ques_list"),
url(r'^studentsection/', views.ques_num, name="ques_num"),
url(r'^replies/', views.replies, name='replies'),
url(r'^logout/', views.logout_view, name='logout'),

]