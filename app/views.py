from django.shortcuts import render
from django.http import HttpResponse

from app.forms import *
# Create your views here.

def insert_topic(request):
    #empty topic form object
    ETFO = TopicForm()
    d ={'ETFO':ETFO}

    if request.method =='POST':
        #topic data form object
        TDFO = TopicForm(request.POST)
        if TDFO.is_valid():
            TDFO.save()
            return HttpResponse('Topic saved successfully')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    
    EWFO = WebpageForm()
    d ={'EWFO':EWFO}

    if request.method =='POST':
        
        WDFO = WebpageForm(request.POST)
        if WDFO.is_valid():
            WDFO.save()
            return HttpResponse('Webpage saved successfully')
        else:
            return HttpResponse('Invalid Data')


    return render(request,'insert_webpage.html',d)


def insert_access(request):
    
    EAFO = AccessRecordForm()
    d ={'EAFO':EAFO}

    if request.method =='POST':
        
        ADFO = AccessRecordForm(request.POST)
        if ADFO.is_valid():
            ADFO.save()
            return HttpResponse('AccessRecord saved successfully')
        else:
            return HttpResponse('Invalid Data')


    return render(request,'insert_access.html',d)
