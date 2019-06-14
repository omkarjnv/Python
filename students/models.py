from django.db import models

class Student(models.Model):
    USN = models.CharField(max_length=10)
    name = models.TextField()
    sem = models.CharField(max_length=1)
    Dept = models.CharField(max_length=10)


    def __str__(self):
        return self.USN

class Teacher(models.Model):
    EID = models.CharField(max_length=10)
    name = models.TextField(max_length=10)
    Dept = models.CharField(max_length=10)
    Contact = models.CharField(max_length=10)

    def __str__(self):
        return self.EID

class Questions(models.Model):
    QNO=models.CharField(max_length=10)
    QID=models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=10,default="nitish123")
    Dept = models.CharField(max_length=10,default="CSE")
    Text= models.TextField()

    def __str__(self):
        return self.QNO

class Reply(models.Model):
    RID = models.ForeignKey(Questions,on_delete=models.CASCADE)
    name=models.CharField(max_length=10,default="nitish123")
    Text= models.TextField()

    

