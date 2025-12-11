from django.shortcuts import render,redirect
from .forms import StudentForm
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='Sign_In')
def add_student(request):
    form = StudentForm()
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
    template_name = 'stu_app/Add_Student.html'
    context = {"form":form}
    return render(request,template_name,context)

@login_required(login_url='Sign_In')
def show_student(request):
    objs = Student.objects.all()
    template_name = 'stu_app/Show_Student.html'
    context = {'records':objs}
    return render(request,template_name,context)

def update_student(request,pk):
    obj = Student.objects.get(stu_id = pk)
    form = StudentForm(instance=obj)
    if(request.method == 'POST'):
        form = StudentForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('Show_Student')
    template_name = 'stu_app/Update_Student.html'
    context = {'form':form}
    return render(request,template_name,context)

def delete_student(request,pk):
    obj = Student.objects.get(stu_id = pk)
    form = StudentForm(instance=obj)
    if(request.method == 'POST'):
        obj.delete()
        return redirect('Show_Student')
    template_name = 'stu_app/Delete_Student.html'
    context = {'obj':obj}
    return render(request,template_name,context)

