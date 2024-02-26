from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.db import connection
from django.db.models import Q, F

# Create your views here.
def UserView(request):
    # return HttpResponse("Hey, I'm Batman!")
    # name = 'Ayan'
    # users = User.objects.all()
    # return render(request, 'user.html', {'users': users})
    # query_set = User.objects.all()
#Using filter with gt
    # filtered_query_set = User.objects.filter(gamesense__gt=5)
#Using filter with range
    # ranged_query_set = User.objects.filter(gamesense__range = (7,15)) 
#objects.all() returns all object. And objects.get() returns a specific object.
    # one = User.objects.get(pk=1)
 #contains is case-sensitive, icontains is not.
    # contains_query_set = User.objects.filter(email__icontains='MeTime')
#filter whose gamesense is less than(lt) 7 and storygames is less than 15
    # complex_query_set = User.objects.filter(gamesense__lt = 7, storygames__lt=15)
#another way to implement the same above thing.
    # complex_query_set = User.objects.filter(gamesense__lt=7).filter(storygames__lt=15)
#Using Q object we can encapsulate a query expression and perform AND, OR operations with them. 
#We import Q class.Use ~ for not: 'not less than 5'.
    # qobject_query_set = User.objects.filter(
    #     Q(gamesense__lt=5) | ~Q(storygames__lt=5))
#We use F object, to filter data while referencing a certain field. Here, we find whose gamesense=storygames. 
    # fobject_query_set = User.objects.filter(gamesense = F('storygames'))
#Sorting queryset. We use - for reverse sorting.
    # sort_query_set = User.objects.order_by('-gamesense', '-storygames')
#Return a queryset which returns three most recent updated queryset 
    threemostrecent_query_set = User.objects.order_by('-updated_at')[0:3]
    return render(request, 'user.html', {'users': threemostrecent_query_set})


def input(request):
    return render(request, 'input.html')


def save_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gamesense = request.POST['gamesense']
        storygames = request.POST['storygames']
        User.objects.create(name=name, email=email, phone=phone, gamesense=gamesense, storygames=storygames)
        return redirect('users_list')
