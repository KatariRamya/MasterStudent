from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from MasterStudentApp.models import Master, Student, Task


# Create your views here.
def index_fun(request):
    return render(request,'index.html')

def masterlon_fun(request):
    return render(request,'MasterLog.html')

def studentlog_fun(request):

    return render(request,'StudentLog.html')

def masterreg_fun(request):
    return render(request,'MasterReg.html')

def studentreg_fun(request):
    return render(request,'StudentReg.html')


def task_fun(request):
    tasks = Task.objects.all()
    return render(request,'task.html',{'data': tasks})

def task_assign(request):
    students = Student.objects.all()

    return render(request, 'AssignTask.html',{'data':students})


def masterreg_readdata(request):
    if request.method == 'POST':
        Name = request.POST['txtname']
        Email = request.POST['txtmbl']
        password = request.POST['txtpwd']
        if Master.objects.filter(Q(Email=Email) | Q(Password=password)).exists():
            return render(request, 'MasterReg.html')
        else:
            m=Master()
            m.Master_Name=request.POST['txtname']
            m.Mobile=request.POST['txtmbl']
            m.Email=request.POST['txtemail']
            m.Password=request.POST['txtpwd']
            m.save()
            return redirect('masterlog',{'data': ''})


def studentreg_readdata(request):
    if request.method == 'POST':
        Name = request.POST['txtname']
        Email = request.POST['txtmbl']
        password = request.POST['txtpwd']
        if Master.objects.filter(Q(Email=Email) | Q(Password=password)).exists():
            return render(request, 'StudentReg.html')
        else:
            s = Student()
            s.Student_Name = request.POST['txtname']
            s.Mobile = request.POST['txtmbl']
            s.Email = request.POST['txtemail']
            s.Password = request.POST['txtpwd']
            s.save()
            return redirect('studentlog')


def read_student_login(request):
    Email = request.POST['txtemail']
    Password = request.POST['txtpwd']
    if Student.objects.filter(Q(Email=Email) & Q(Password=Password)).exists():
        return render(request, 'student_dash.html')
    else:
        return render(request, 'studentlog.html')


def read_master_login(request):
    Email = request.POST['txtemail']
    Password = request.POST['txtpwd']
    if Master.objects.filter(Q(Email=Email) & Q(Password=Password)).exists():
        return render(request, 'master_dash.html')
    else:
        return render(request, 'MasterLog.html')


class HttpReponse:
    pass


def taskreaddata_fun(request):
    l=Task()
    l.Left=request.POST['ddlleft']
    l.Operation=request.POST['ddloper']
    l.Right=request.POST['ddlright']
    l.Students=Student.objects.get(Student_Name=request.POST['ddlstudent'])
    l.save()


    s = Student.objects.all()
    return redirect('AssignTask')

    # return render(request,'AssignTask.html',{'data':s})


def logout_fun(request):
    return redirect('home')


def solve(request,id):
    t1 = Task.objects.get(id=id)
    left = t1.Left
    left = globals()[left]
    right = t1.Right
    right = globals()[right]
    op = t1.Operation
    op = globals()[op]
    print(left,right)

    res = left(op(right()))
    t1.Complete = True
    return  render(request,'task.html',{'sol': f'solution is{res}','data':Task.objects.all()})


def make_num(num,func):
    if func == None:
        return num
    else:
        return func(num)


def zero(func= None):
    return make_num(0,func)


def one(func= None):
    return make_num(1,func)


def two(func= None):
    return make_num(2, func)


def three(func= None):
    return make_num(3,func)


def four(func= None):
    return make_num(4,func)


def five(func= None):
    return make_num(5,func)


def six(func= None):
    return make_num(6,func)


def seven(func = None):
    return make_num(7, func)


def eight(func=None):
    return make_num(8, func)

def nine(func= None):
    return make_num(9, func)

def times(right):
  sum = lambda left :  left * right
  return  sum

def plus(right):
  sum = lambda left :  left + right
  return  sum

def minus(right):
  sum = lambda left :  left - right
  return  sum

def divided_by(right):
  sum = lambda left :  left // right
  return  sum