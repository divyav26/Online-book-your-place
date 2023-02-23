from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Place,State
import requests
from .forms import ContactForm
import json
from testapp.forms import SignUpForm
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import LineItemFormset, InvoiceForm

# Create your views here.
def home(request):
    cats=State.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        print('-----',q)
        state=State.objects.filter(title__icontains=q).order_by('-id')
        print(state)
    else:
        state=State.objects.all().order_by('-id')
    paginator=Paginator(state,3)
    page_number=request.GET.get('page')
    try:
        state=paginator.page(page_number)
    except PageNotAnInteger:
        state=paginator.page(1)
    except EmptyPage:
        state=paginator.page(paginator.num_pages)
    return render(request,'testapp/home.html',{'state':state,'cats':cats})

    #return render(request,'testapp/home.html',{'cats':cats})
def all_news(request):
    all_news=Place.objects.all()
    return render(request,'testapp/home.html',{'all_news':all_news})
def all_category(request):
    cats = State.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        print('-----', q)
        state = State.objects.filter(title__icontains=q).order_by('-id')
        print(state)
    else:
        state = State.objects.all().order_by('-id')
    paginator = Paginator(state, 3)
    page_number = request.GET.get('page')
    try:
        state = paginator.page(page_number)
    except PageNotAnInteger:
        state = paginator.page(1)
    except EmptyPage:
        state = paginator.page(paginator.num_pages)
    return render(request, 'testapp/all_category.html', {'state': state, 'cats': cats})

# Fetch all category
# def category(request,id):
#     category=State.objects.get(id=id)
#     print('--------',category)
#     # news=Place.objects.filter(category=category)
#     # if 'place' in request.GET:
#     #     place=request.GET['place']
#     #     print('-----',place)
#     #     place=Place.objects.filter(title__icontains=place).order_by('-id')
#     #     print(place)
#     # else:
#     #     place=Place.objects.all().order_by('-id')
#     news=Place.objects.filter(category=category)
#     if 'place' in request.GET:
#         news=request.GET['place']
#         print('-----',news)
#         news=Place.objects.filter(title__icontains=news).order_by('-id')
#         print(news)
#     else:
#         news=Place.objects.filter(category=category)
#
#     return render(request,'testapp/state-place.html',{'all_news':news,'category':category})
##  copy
def category(request,id):
    category=State.objects.get(id=id)
    print('--------',category)
    news=Place.objects.filter(category=category)
    if 'place' in request.GET:
        news=request.GET['place']
        print('-----',news)
        news=Place.objects.filter(title__icontains=news).order_by('-id')
        print(news)
    else:
        news=Place.objects.filter(category=category)

    return render(request,'testapp/state-place.html',{'all_news':news,'category':category})

# Detail Page
def detail(request,id):
    news=Place.objects.get(pk=id)
    category=State.objects.get(id=news.category.id)
    rel_news=Place.objects.filter(category=category).exclude(id=id)
    return render(request,'testapp/detail.html',{'news':news,'related_news':rel_news})

def send_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    querystring={"authorization":"NUSmKAdxT8aL3j7ZEr56kORgCWlqhzeDiyFMs1VXtGbPQn0ovHlK56HMr13VevJ2EfCkLhXI4buZyjic","sender_id":"FSTSMS","message":message,"language":"english","route":"p","numbers":number}
    responce=requests.get(url,params=querystring)
    dic=responce.json()

@login_required
def payment(request):
    all_news=Place.objects.all()
    if request.method == 'POST':
        url = "https://www.fast2sms.com/dev/bulk"
        print('It Works')
        phone = request.POST['username']
        user = request.POST['user']
        message_sms = 'Dear {} Book Successfully'.format(user)
        print('-----phone',phone)
        print('message_sms',message_sms)
        send_sms(phone,message_sms)
        return render(request,'testapp/success.html')
    return render(request,'testapp/p.html',{'all_news':all_news})


def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})


def logout(request):
    return render(request,'testapp/logout.html')

def add_people(request):
    form=InvoiceForm()
    # if request.method=='POST':
    #     form=SignUpForm(request.POST)
    #     user=form.save()
    #     user.set_password(user.password)
    #     user.save()
    #     return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/add_people.html',{'form':form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Thank For Contact!!!')
    else:
        form = ContactForm()
    return render(request,'testapp/contact.html',{'form':form})