from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# def home(request):
#     return HttpResponse("<h1>Welcome to Student Management System</h1>")

from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def list(request):
    return render(request, "list.html")

def base(request):
    return render(request, "base.html")

def model(request):
    return render(request, "model.html")


from .models import Student
@login_required
def student_list(request):
    students = Student.objects.all()#student hamro model
#student variable,object.all le sabai tanxa as email,name,other datas.
    return render(
        request,
        "students/studentlist.html",
        {"students": students}
        #suru ma make stdent vane function,ani data tanera aafu ma ara basxu ani lastly frontend ma phatako .
    )

from django.shortcuts import render, redirect #logic redirection konkam garxa 
from .forms import StudentForm
#student form tanara rakhim 
@login_required
def student_create(request):

    if request.method == "POST":#post mean user le form submit gareko .
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()#save hunxa so dtata base ma aayera basxaaa
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )

from django.shortcuts import get_object_or_404

@login_required
def student_update(request, student_id):

    student = get_object_or_404(#get le baneko xaina vane khojera leuxa.
        Student,
        id=student_id
    )

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)#as like save extra part.

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )

@login_required
def student_delete(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "register/register.html",
        {"form": form}
    )


def login_view(request):
    return render(request, "register/login.html")



def logout_view(request):
    return render(request, "register/logout.html")