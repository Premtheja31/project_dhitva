from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    Data=DataStorage.objects.all()
    d={'Data':Data}
    if request.method=='POST':
        n=request.POST['name']
        tenth=request.POST['tenth']
        inter=request.POST['inter']
        degree=request.POST['degree']
        mob=request.POST['mobile']
        ma=request.POST['mail']
        skill=request.POST['skills']
        work=request.POST['work']
        ds=DataStorage(name=n,tenth_marks=tenth,inter_marks=inter,degree_marks=degree,mobile=mob,mail=ma,skills=skill,work_experience=work)
        ds.save()
        return render(request,'response.html')
    return render(request,'home.html',d)