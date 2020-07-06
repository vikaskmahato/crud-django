from django.shortcuts import render, HttpResponseRedirect
from .forms import Register
from .models import Profile

def addshow(request):
    if request.method=='POST':
        fm=Register(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=Profile(name=nm, email=em, password=pw)
            reg.save()
            fm=Register()
    else:
        fm=Register()
    inf=Profile.objects.all()
    return render(request, 'addandshow.html',{'form':fm,'info':inf})    

def deletedata(request, id):
    if request.method=='POST':
        p=Profile.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect('/')

def updatedata(request, id):
    if request.method=='POST':
        p=Profile.objects.get(pk=id)
        fm=Register(request.POST, instance=p)
        if fm.is_valid():
            fm.save()
    else:
            p=Profile.objects.get(pk=id)
            fm=Register(instance=p)
    return  render(request, 'update.html',{'form':fm})       




