from django.shortcuts import render
from app.models import *
from app.forms import *
# Create your views here.


def home(request):
    return render(request,'index.html')
def display(request):
    form=Demoform
    if request.method =='POST':
        form=Demoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app/display.html',{'form':form})
def show(request):
    url='https://www.etsy.com/in-en/?ref=lgo'
    result=student.objects.all()
    return render(request,'app/show.html',{'result':result})
def update(request,id):
    s=student.objects.get(id=id)
    form=Demoform(instance=s)
    if request.method=='POST':
        form= Demoform(request.POST,instance=s)
        if form.is_valid():
            form.save()
    return render(request, 'app/update.html',{'form':form})
def delete(request,id):
    s=student.objects.get(id=id)
    s.delete()
    return show(request)