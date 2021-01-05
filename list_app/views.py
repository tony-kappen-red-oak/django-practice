from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseNotAllowed,HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Item
# Create your views here.
def index(request):
    return render(request,"index.html")
def list_view(request,pk):
    return render(request,'list.html',{
        'id':pk,
    })
def add_task(request,pk):
    print("here!")
    task = request.POST["task"]
    prio = request.POST["priority"]
    user = User.objects.get(pk = pk)
    print(pk)
    print(task)
    print(prio)
    i = Item()
    i.item_owner_id = user
    i.item_prio = prio
    i.item_text = task
    print(i)
    i.save()
    return HttpResponse("hello")
    # return HttpResponseRedirect(reverse(request,"list_view",args=(id,)))
def loginOrSignUp(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        users = User.objects.filter(username=username)
        if len(users) == 0:
            #sign up
            u = User(is_superuser=False,username=username,password=password)
            u.save()
            return HttpResponseRedirect(reverse('list_view',args=(u.pk,)))
        else:
            user = users[0] 
            if user.password == password:
                #grant access
                return HttpResponseRedirect(reverse('list_view',args=(user.pk,)))
            else:
                return HttpResponseNotAllowed("Wrong username/password")
            pass
    else:
        return HttpResponseNotFound("Not Found!")