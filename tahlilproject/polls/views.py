from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .models import Neighbor , RequestLetter
from .models import Apartment
from .models import Charge , Bill
from django.conf import settings
from django.forms import modelformset_factory
from django.contrib.auth import authenticate, login

from django.shortcuts import get_object_or_404, render

from django.template import loader
# Create your views here.

from .forms import LoginForm
from django.contrib.auth.models import User

def loginView(request):
    # if request.user.is_authenticated():
    #     redirect('polls/index.html')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password']);
            if user is not None:
                login(request, user)
                return render(request, 'polls/login2.html')
            # else:
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def mainpage1(request):
   # ApartmentFormSet = modelformset_factory(Apartment , fields=('number' , 'floor_num'))
   # formset = ApartmentFormSet()
   #  return render(request, 'polls/index.html' , {'id' : id})
    return HttpResponse("hello world")

def mainpage(request , id):
   # ApartmentFormSet = modelformset_factory(Apartment , fields=('number' , 'floor_num'))
   # formset = ApartmentFormSet()
    return render(request, 'polls/index.html' , {'id' : id})

def financial(request , id , type):
    print('chtoriiiii', id)
    neighbor = get_object_or_404(Neighbor , pk=id)
    print('salammmmm')
    print(neighbor.neighbor_family_name)
    apartment = neighbor.apartment
    return render(request, 'polls/financial.html', {'type' : type , 'id': id , 'apartment':apartment})

def reservation(request , id , reserve):
    return render(request, 'polls/reservation.html' , {'hasreserve' : reserve , 'id' : id})

def neighbors(request , id):
    neighbor = Neighbor.objects.get(pk=id)
    return render(request , 'polls/neighbors.html' , {'id': id , 'Neighbor':Neighbor.objects , 'is_modir':(Neighbor.objects.get(pk=id).type == 'modir') , 'Messages':RequestLetter.objects.filter(receiver=neighbor)})

def guest(request , id , guest_id):
    return render(request , 'polls/guest.html' , {'id' : id , 'guest_id' : guest_id , 'is_modir':(Neighbor.objects.get(pk=id).type == 'modir')})

def validation(request , id):
    return render(request , 'polls/validation.html' , {'id' : id})

def owner(request , id):
    return render(request, 'polls/owner.html', {'id': id})

def pay(request , id , type , pay):
    print('im in!')
    if(type == 'bill'):
        bill = Bill.objects.get(pk=pay)
        bill.is_payed = True
        bill.save()
        print('payement',pay)
    if(type == 'charge'):
        charge = Charge.objects.get(pk=pay)
        charge.is_payed = True
        charge.save()
    return HttpResponseRedirect(reverse('financial', args=(id , type)))


def guest_request(request , id , guest_id):
    sender = Neighbor.objects.get(pk=id)
    receiver = Neighbor.objects.get(pk=guest_id)
    requestLetter = RequestLetter(sender = sender , receiver= receiver , type=request.POST.get('category' , False) , text=request.POST.get('content' , False) , title=request.POST.get('title' , False))
    requestLetter.save()
    return HttpResponseRedirect(reverse('neighbors', args=(id,)))


def neighbors_add(request , id):
    neighbor = Neighbor(neighbor_name=request.POST.get('name',False) , neighbor_family_name=request.POST.get('family_name',False) , national_id=request.POST.get('national_id',False))
    print('victory!')
    neighbor.save()
    return HttpResponseRedirect(reverse('neighbors', args=(id,)))