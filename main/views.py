from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm


# Create your views here.
def register (request):
	if request.user.is_authenticated:
		return redirect('main:index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

def loginpage (request):
	if request.user.is_authenticated:
		return redirect('main:index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('main:index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)

def logoutUser (request):
	logout(request)
	return redirect('main:login')

def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

	return redirect(reverse('main:success', args=[amount]))

def successMsg(request, args):
	amount = args
	return render(request, 'main/success.html', {'amount':amount})

def index (request): 
    return render(request, 'main/index.html')

def about (request): 
    return render(request, 'main/about.html')

def contact (request): 
    return render(request, 'main/contact.html')

def causes (request): 
    return render(request, 'main/causes.html')

def portfolio (request): 
    return render(request, 'main/portfolio.html')

def education (request): 
    return render(request, 'main/education.html')

def courses (request): 
    return render(request, 'main/courses.html')

def schedule (request): 
    return render(request, 'main/schedule.html')

def singlecauses (request): 
    return render(request, 'main/single-causes.html')

def donation (request): 
    return render(request, 'main/donation.html')









