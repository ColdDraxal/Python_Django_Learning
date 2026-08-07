from django.shortcuts import render
from django.http import HttpResponse
from sport.models import Sport
# Create your views here.

def Home(request):
    # return HttpResponse(' <h1> Landing Page... </h1>')
    return render(request, 'landing.html')

def About(request):
    # return HttpResponse('<h1> About us.... </h1>')
    return render(request, 'about.html')


def Service(request):
    return render(request, 'service.html')

def Contact(request):
    return render(request, 'contact.html')

def StudentbyId(request,id):
    # return HttpResponse(f'<h1> Student id is : {id}</h1>')
    context ={
        "id":id
    }
    return render('request','Student/StudentByID.html',context)

def SearchParam(request,name):
    # return HttpResponse(f'<h1> Student name is : {name}</h1>')
    context ={
        "str":name
    }
    return render(request, 'Search/search.html',context)

def productdetail(request,item):
    context={
        "name":item
    }
    return render(request,'Product/product.html',context)

# file/image/photo/image.jpg
def Files(request,file_path):
    print(file_path)
    return HttpResponse(f'<h1>File Path is : {file_path}</h1>')

def Index(request):
    sport = Sport.objects.all()  #get all the data from the Sport model
    context = {
        'sports':sport
    }
    print(sport)
    return render(request,'index.html', context)