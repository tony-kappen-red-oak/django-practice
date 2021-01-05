from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseNotAllowed,HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Item
import json
# Create your views here.
def index(request):
    return render(request,"index.html")
def list_view(request,pk):
    u = User.objects.get(pk=pk)
    i = Item.objects.filter(item_owner_id=u,item_done=False)
    i = i.order_by('item_prio')
    print(i)
    return render(request,'list.html',{
        'user':u,
        'items':i,
    })
def save_tasks(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    data = body['data']
    for i in data:
        item = Item.objects.get(pk=i['id'])
        if i['is_done']:
            item.delete()
        else:
            item.item_prio = i['priority']
            item.save()
    return HttpResponse("saved!")
def add_task(request,pk):
    task = request.POST["task"]
    prio = request.POST["priority"]
    user = User.objects.get(pk = pk)
    i = Item()
    i.item_owner_id = user
    i.item_prio = prio
    i.item_text = task
    i.save()
    return HttpResponseRedirect(reverse("list_view",args=(pk,)))
def loginOrSignUp(request):
    if request.method == "POST":
        try:
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
        except(e):
            print(e)
    else:
        return HttpResponseNotFound("Not Found!")