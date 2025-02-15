from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
import random
# Create your views here.
def home(request):
    un = request.session.get('username')
    if un:
        UO = User.objects.get(username=un)
        d = {'UO': UO}
        return render(request, 'home.html', d)
    return render(request,'home.html')


def register(request):
    EUFO = UserForm()
    d = {'EUFO':EUFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        if UFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            message = f"Hello {MUFDO.username}, \n Thank You For Registering to our website, with pno {MPFDO.pno}\n \n Thanks & regards \n \t Team"
            email = MUFDO.email
            send_mail(
                "Thanks For Registration",
                message,
                'debajyotin56@gmail.com',
                [email],
                fail_silently=False
            )
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('INVALID DATA')
    return render(request,'register.html', d)


def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        AUO = authenticate(username=un, password=pw)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username'] = un
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('invalid creds')
    return render(request,'user_login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def create_contact(request):
    un = request.session.get('username')
    if un:
        if request.method == 'POST' and request.FILES:
            UO = User.objects.get(username=un)
            CFDO = ContactForm(request.POST, request.FILES)
            MCFDO = CFDO.save(commit=False)
            MCFDO.username=UO
            MCFDO.save()
            return HttpResponseRedirect(reverse('home'))
        ECFO = ContactForm()
        d = {'ECFO': ECFO}
        return render(request, 'create_contact.html', d)
    return HttpResponseRedirect(reverse('user_login'))

def display(request, pk):
    un = request.session.get('username')
    if un:
        CO = Contact.objects.get(pk=pk)
        d = {'CO': CO}
        return render(request, 'display.html', d)
    return HttpResponseRedirect(reverse('user_login'))


def update(request, pk):
    un = request.session.get('username')
    if un:
        CO = Contact.objects.get(pk=pk)
        d = {'CO': CO}
        if request.method == 'POST':
            name = request.POST.get('name')
            add = request.POST.get('add')
            email = request.POST.get('email')
            CO.name=name
            CO.add=add
            CO.email=email
            return HttpResponseRedirect(reverse('home'))
        return render(request, 'update.html', d)
    return HttpResponseRedirect(reverse('user_login'))


def delete(request, pk):
    un = request.session.get('username')
    if un:
        CO = Contact.objects.get(pk=pk)
        CO.delete()
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('user_login'))


def search(request):
    if request.method == 'POST':
        pk = request.POST.get('search')
        print(pk)
        CO = Contact.objects.get(pk=pk)
        d = {'CO': CO}
    return render(request, 'display.html', d)
    
def un(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        UO = User.objects.get(username=un)
        if UO:
            otp = random.randint(1000, 9999)
            print(otp)
            request.session['username']=un
            request.session['otp'] = otp
            return HttpResponseRedirect(reverse('loginotp'))
        return HttpResponse('User Not Found')
    return render(request, 'un.html')

def otp(request):
    if request.method == 'POST':
        uotp = request.POST.get('otp')
        gotp = request.session.get('otp')
        if int(uotp) == gotp:
            return HttpResponseRedirect(reverse('change_pw'))
        else:
            return HttpResponse('invalid otp')
    return render(request, 'otp.html')


def change_pw(request):
    if request.method == 'POST':
        pw = request.POST.get('pw')
        cpw = request.POST.get('cpw')
        if pw == cpw:
            un = request.session.get('username')
            UO = User.objects.get(username=un)
            UO.set_password(pw)
            UO.save()
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('password miss mathched')
    return render(request, 'change_pw.html')


def loginotp(request):
    if request.method == 'POST':
        uotp = request.POST.get('otp')
        gotp = request.session.get('otp')
        if int(uotp) == gotp:
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid otp')
    return render(request, 'loginotp.html')



def login_with_otp(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        UO = User.objects.get(username=un)
        if UO:
            otp = random.randint(1000, 9999)
            print(otp)
            request.session['otp'] = otp
            return HttpResponseRedirect(reverse('loginotp'))
        else:
            return HttpResponse('Username not valid')
    return render(request,'login_with_otp.html')


