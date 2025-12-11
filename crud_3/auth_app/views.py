from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Sign_In')
    template_name = 'auth_app/Sign_Up.html'
    context = {'form':form}
    return render(request,template_name,context)

def sign_in(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password) 
        if(user is not None):
            login(request,user)
            return redirect('Show_Student')
        return redirect('Sign_Up')
    template_name = 'auth_app/sign_in.html'
    context = {}
    return render(request,template_name,context)

def sign_out(request):
    logout(request)
    return redirect('Sign_In')

