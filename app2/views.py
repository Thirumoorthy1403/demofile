from django.shortcuts import render
# Create your views here.

def demo(request):
    return render(request,'app2/demo.html')
def demo1(request):
    return render(request,'app2/demo1.html')
def demo2(request):
    return render(request,'app2/demo2.html')
def demo3(request):
    return render(request,'app2/demo3.html')

