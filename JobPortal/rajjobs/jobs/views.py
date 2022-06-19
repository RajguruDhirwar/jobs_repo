from django.shortcuts import render
from jobs.models import Hydjobs,Banglorejbs,Punejobs
# Create your views here.

def homepage_view(request):
    return render(request,'jobs/index.html')


def hydjobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobs/hydjobs.html',context=my_dict)

def banglorejbs_view(request):
    jobs_list1 = Banglorejbs.objects.all()
    my_dict = {'jobs_list1':jobs_list1}
    return render(request,'jobs/banglorejbs.html',context=my_dict)

def punejobs_view(request):
    jobs_list2 = Punejobs.objects.all()
    my_dict = {'jobs_list2':jobs_list2}
    return render(request,'jobs/punejobs.html',context=my_dict)
