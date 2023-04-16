from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        To.save()
        return HttpResponse('Topic inserted')

    return render(request,'insert_topic.html')


def insert_Webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=topic)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage insertion is done Successfully')


    return render(request,'insert_Webpage.html',d)




def insert_AccessRecord(request):
    if request.method=="POST":
        name=request.POST['name']
        WO=Webpage.objects.get_or_create(name=name)[0]
        WO.save()
        

        at=request.POST['at']
        d=request.POST['d']
        print(request.POST)
        
        AO=AccessRecord.objects.get_or_create(name=WO,author=at,date=d)[0]
        AO.save()

        return HttpResponse('Accessrecords inserted is done successfully')

    return render(request,'insert_AccessRecord.html')
