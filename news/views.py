from django.shortcuts import render
import requests
# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def newspage(request):
    return render(request,'news.html')

def sportspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    response = url.json()
    sportdata = response['data']
    context={
        "sportnews":sportdata
    }
    return render(request,'sports.html',context)

def politicspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=politics")
    response = url.json()
    politicsdata = response['data']
    context = {
        "politicsnews": politicsdata
    }
    return render(request,"politics.html",context)

def technologypage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=technology")
    response = url.json()
    technologydata = response['data']
    context = {
        "technologynews": technologydata
    }
    return render(request,"technology.html",context)

def businesspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=business")
    response = url.json()
    businessdata = response['data']
    context = {
        "businessnews": businessdata
    }
    return render(request,"business.html",context)

def automobilepage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=automobile")
    response = url.json()
    automobiledata = response['data']
    context = {
        "automobilenews": automobiledata
    }
    return render(request,"automobile.html",context)

def sicencepage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=science")
    response = url.json()
    sciencedata = response['data']
    context = {
        "sciencenews": sciencedata
    }
    return render(request,"science.html",context)

def allnewspage(request):
    return render(request,"all-news.html")

def searchapi(request):
    s=request.POST.get("search")
   # print(s)

    url = requests.get("https://inshortsapi.vercel.app/news?category="+s)
    response = url.json()
    allnewsdata = response['data']
    context = {
        "allnewsdata": allnewsdata
    }
    return render(request,"all-news.html",context)