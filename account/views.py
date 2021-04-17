from django.shortcuts import render
from account.models import Profile
from account.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json


def SaveData(request):
    saved = False
    print('Entered')
    if request.method == "POST":
        jfile= request.FILES['jfile']
        data=jfile.read()
        for i in json.loads(data):
            profile=Profile(userid=i['userId'],id=i['id'],title=i['title'],body=i['body'])
            try:
                profile.save()
            except :
                e = sys.exc_info()[0]
                print(e)
    return HttpResponseRedirect('show')
 
@login_required 
def show(request):  
    profiles = Profile.objects.all()  
    return render(request,"account/show.html",{'profiles':profiles}) 
	
	
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return render(request, 'account/login.html', {})
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'account/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
						   
						   
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'account/index.html',{'username':username})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'account/login.html',{})
		

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'account/login.html', {})