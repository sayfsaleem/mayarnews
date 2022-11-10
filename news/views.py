from django.http import HttpResponse
from django.shortcuts import render
from news.models import News,Category, SocialPage

# Create your views here.
def home(request):
    # loading data from db 
    all = News.objects.all()[:10]
    news = News.objects.order_by('date')
    fet = News.objects.order_by('date')[:20]
    newss = reversed(news)
    side = news[0:1]
    sided = reversed(fet)
    cats = Category.objects.all()
    postmain = News.objects.order_by('date')[:30]
    main = reversed(postmain)
    social = SocialPage.objects.all()
    tranding = reversed(News.objects.order_by('date')[:3])
    data = {
        'news' : newss ,
        'side' : side,
        'cats' : cats,
        'sided' : sided ,
        'fet' : fet ,
        'main' : main ,
        'social' : social,
        'tranding' : tranding ,
    }
    return render(request, 'index.html',data)

def post(request,url): 
    onenews = News.objects.get(url=url)
    return render(request,'post.html',{'post':onenews})

def contact(request):
    social = SocialPage.objects.all()
    return render(request,'contact.html',{'social':social ,})