from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.db import connection

# Create your views here.
def UserView(request):
    #return HttpResponse("Hey, I'm Batman!")
    #name = 'Ayan'
    #queryset = User.objects.raw('SELECT * FROM testapp_user')
    #return render(request, 'dummy.html', {'name': name, 'result': list(queryset)})
    users = User.objects.all()
    return render(request, 'user.html', {'users': users})


def input(request):
    return render(request, 'input.html')


def save_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gamesense = request.POST['gamesense']
        User.objects.create(name=name, email=email, phone=phone, gamesense=gamesense)
        return redirect('users_list')