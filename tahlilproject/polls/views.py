from django.shortcuts import render
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .models import Neighbor , RequestLetter, Facility, AvailableTimes
from .models import Apartment, Building, Warning, MonthlyPayment, WarningLetter
from .models import Charge , Bill, Dashboard, WarningLetter, Reservation, Bank
from django.conf import settings
from django.forms import modelformset_factory
from django.contrib.auth import authenticate, login, logout
from datetime import date
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from django.template import loader
# Create your views here.

from .forms import LoginForm, bankForm, AddDashbordForm, signUpForm, AddFacilityForm, SendMessageForm, EditProfileForm
from .forms import AddBuilding, AddApartment, AddBill, OwnerWarningForm, OwnerContractForm
from django.contrib.auth.models import User

#registeration, login and logout:
def logoutView(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    logout(request)
    return HttpResponseRedirect('/login/')

def signupView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('../home/index/')
    if request.method == 'GET':
        form = signUpForm()
        context = {}
        context['form'] = form
        return render(request, 'polls/signUp.html', context)
    else:
        form = signUpForm(request.POST)
        if (form.is_valid()):
            user = User(username=request.POST['firstName'], password=request.POST['password'], email=request.POST['emailAddress'], first_name=request.POST['firstName'], last_name=request.POST['lastName'])
            user.set_password(request.POST['password'])
            user.save()
            neighbor = Neighbor(user=user, national_id=request.POST['nationalID'], sex=request.POST['sex'], type='neighbor', bank_account=request.POST['bankAccount'])
            neighbor.apartment = Apartment.objects.get(id=request.POST['apartmentID'])
            neighbor.bank = Bank.objects.get(name=request.POST['bank'])
            neighbor.save()
            form = LoginForm()
            context = {}
            context['form'] = form
            return render(request, 'registration/login.html', context)
        context = {}
        context['form'] = form
        return render(request, 'polls/signUp.html', context)

def loginView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('../home/index/')
    if request.method == 'POST':
        # if 'signup' in request.POST:
        #     form = signUpForm()
        #     context = {}
        #     context['form'] = form
        #     return render(request, 'polls/signUp.html', context)
        #     # return HttpResponseRedirect('../signup/')
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                # return redirect('/home/index.html')
                return HttpResponseRedirect('../home/index/')
            # else:
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})






#main parts:
def removeFromDashbord(request, id):
    username = None
    if request.user.is_authenticated():
        user = Neighbor.objects.get(   user = User.objects.get(username = request.user.get_username())   )
        if (user.type != 'admin'):
            return HttpResponseRedirect("../")
        dashbord = Dashboard.objects.get(id= id)
        dashbord.delete()
        return HttpResponseRedirect("../")
    return HttpResponseRedirect("../")

def removeNeighbor(request, username):
    if request.user.is_authenticated():
        user = Neighbor.objects.get(user=User.objects.get(username=request.user.get_username()))
        neighbor = Neighbor.objects.get(user__username=username)
        if user.type == 'admin' and user.apartment.building == neighbor.apartment.building and neighbor.type == 'neighbor':
            neighbor.delete()
            User.objects.get(username = username).delete()
    return HttpResponseRedirect("/neighbors/")

def index(request):
    username = None
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/../login/')
    if request.user.is_authenticated():
        user = Neighbor.objects.get(   user = User.objects.get(username = request.user.get_username())   )
        context = {}
        context['user']=user
        dashbords = Dashboard.objects.filter(_building=user.apartment.building).order_by('-date_time')
        context['dashbords'] = dashbords
        messages = RequestLetter.objects.filter(receiver=user).order_by('-date_time')
        context['messages'] = messages
        # warnings = WarningLetter.objects.filter()
        warnings = Warning.objects.filter(receiving_neighbor=user)
        context['warnings'] = warnings

        # for admin:
        if user.type == "admin":
            addDashbordForm = AddDashbordForm()
            context['addDashbordForm'] = addDashbordForm

        #processing inputs
        if user.type == 'admin':
            if request.method == 'POST':
                if 'addToDashbord' in request.POST:
                    newDashbordForm = AddDashbordForm(request.POST)
                    if (newDashbordForm.is_valid()):
                        newTmp = Dashboard(title=request.POST['title'], text = request.POST['text'], date_time= datetime.datetime.now(), _building=user.apartment.building)
                        newTmp.save()
                # elif 'removeFromDashbord' in request.POST:

        if request.method == 'POST':
            if 'sendingMessage' in request.POST:
                sendMessageForm = SendMessageForm(request.POST)
                if (sendMessageForm.is_valid()):
                    recievers = sendMessageForm.cleaned_data['recievers']
                    title = sendMessageForm.cleaned_data['title']
                    type = sendMessageForm.cleaned_data['type']
                    text = sendMessageForm.cleaned_data['text']
                    allRecievers = recievers.split(';')
                    for recieverUsername in allRecievers:
                        if Neighbor.objects.filter(user__username=recieverUsername ).exists():
                            reciever = Neighbor.objects.get(user__username=recieverUsername )
                            tmpMessage = RequestLetter(sender=user, receiver=reciever, title=title, type=type, text=text, date_time=datetime.datetime.now())
                            tmpMessage.save()
        sendMessageForm = SendMessageForm()
        context['sendMessageForm'] = sendMessageForm


        if request.method == 'POST':
            if 'editingProfile' in request.POST:
                editProfileForm = EditProfileForm(request.POST)
                if editProfileForm.is_valid():
                    firstName = editProfileForm.cleaned_data['firstName']
                    lastName = editProfileForm.cleaned_data['lastName']
                    email = editProfileForm.cleaned_data['emailAddress']
                    apartmentID = editProfileForm.cleaned_data['apartmentID']
                    bankName = editProfileForm.cleaned_data['bank']
                    bankAccount = editProfileForm.cleaned_data['bankAccount']

                    user.user.first_name = firstName
                    user.user.last_name = lastName
                    user.user.email = email
                    if Apartment.objects.filter(id=apartmentID).exists():
                        user.apartment = Apartment.objects.get(id = apartmentID)
                    if Bank.objects.filter(name=bankName).exists():
                        user._bank = Bank.objects.get(name=bankName)
                    user.bank_account = bankAccount
                    user.save()

        editProfileForm = EditProfileForm()
        context['editProfileForm'] = editProfileForm

        if user.type == 'admin':
            if request.method == 'POST':
                if 'addingBuilding' in request.POST:
                    addBuilding = AddBuilding(request.POST)
                    if addBuilding.is_valid():
                        postalCode = addBuilding.cleaned_data['postalCode']
                        city = addBuilding.cleaned_data['city']
                        street = addBuilding.cleaned_data['street']
                        number = addBuilding.cleaned_data['number']
                        newBuilding = Building(postal_code= postalCode, city = city, street = street, number= number)
                        newBuilding.save()

                if 'addingApartment' in request.POST:
                    addApartment = AddApartment(request.POST)
                    if addApartment.is_valid():
                        if Building.objects.filter(postal_code = addApartment.cleaned_data['buildingPostalCode']).exists():
                            building = Building.objects.get(postal_code = addApartment.cleaned_data['buildingPostalCode'])
                            floor = addApartment.cleaned_data['floor']
                            newApartment = Apartment(building= building, floor = floor)
                            newApartment.save()

                if 'addingNeighbor' in request.POST:
                    form = signUpForm(request.POST)
                    if (form.is_valid()):
                        user = User(username=request.POST['firstName'], password=request.POST['password'],
                                    email=request.POST['emailAddress'], first_name=request.POST['firstName'],
                                    last_name=request.POST['lastName'])
                        user.set_password(request.POST['password'])
                        neighbor = Neighbor(national_id=request.POST['nationalID'], sex=request.POST['sex'],
                                            type=request.POST['type'] , bank_account=request.POST['bankAccount'])
                        neighbor.apartment = Apartment.objects.get(id=request.POST['apartmentID'])
                        neighbor.bank = Bank.objects.get(name=request.POST['bank'])
                        neighbor.bank_account = form.cleaned_data['bankAccount']
                        user.save()
                        neighbor.user = user
                        neighbor.save()


            addBuilding= AddBuilding()
            context['addBuilding'] = addBuilding

            addApartment = AddApartment()
            context['addApartment'] = addApartment

            addNeighbor = signUpForm()
            context['addNeighbor'] = addNeighbor

            allComplaints = WarningLetter.objects.all().order_by('-date')
            context['allComplaints'] = allComplaints

        user = Neighbor.objects.get(user=User.objects.get(username=request.user.get_username()))

        context['date'] = date.today();

        allWarnings = Warning.objects.filter(receiving_neighbor=user)
        context['allWarnings'] = allWarnings

        return render(request, 'polls/index.html', context)
    return render(request, 'polls/facility.html', {}) #todo

def neighbors(request):
    if request.user.is_authenticated():
        user = Neighbor.objects.get(     user = User.objects.get(      username=request.user.get_username())    )
        context = {}
        context['user'] = user
        p = Neighbor.objects.all().order_by('-user__last_login')
        context['neighbors'] = p #todo
        return render(request, 'polls/neighbors.html', context)
    return render(request, 'polls/facility.html', {})  # todo

def detailsNeighbor(request, username):
    if request.user.is_authenticated():
        user = Neighbor.objects.get(     user = User.objects.get(      username=request.user.get_username())    )

        neighbor = Neighbor.objects.get(user__username=username)

        context = {}
        context['neighbor'] = neighbor

        context['user'] = user

        context['date'] = date.today();

        if user.type == 'admin' and user.apartment.building == neighbor.apartment.building:
            allBills = Bill.objects.filter(_apartment=neighbor.apartment).order_by('-due_date')
            context['allBills'] = allBills
            allCharges = Charge.objects.filter(_apartment=neighbor.apartment).order_by('-due_date')
            context['allCharges'] = allCharges
            if request.method == 'POST':
                if 'addingBill' in request.POST:
                    addBill = AddBill(request.POST)
                    if addBill.is_valid():
                        title = addBill.cleaned_data['title']
                        price = addBill.cleaned_data['price']
                        due_date = addBill.cleaned_data['due_date']
                        apartment = neighbor.apartment
                        newBill = Bill(title = title, price = price, due_date=due_date, _apartment=apartment, is_payed=False)
                        newBill.save()

                if 'addingCharge' in request.POST:
                    addCharge = AddBill(request.POST)
                    if addCharge.is_valid():
                        title = addCharge.cleaned_data['title']
                        price = addCharge.cleaned_data['price']
                        due_date = addCharge.cleaned_data['due_date']
                        apartment = neighbor.apartment
                        newCharge = Charge(title = title, price = price, due_date=due_date, _apartment=apartment, is_payed=False)
                        newCharge.save()

            addBill = AddBill()
            context['addBill'] =addBill

            addCharge = AddBill()
            context['addCharge'] = addCharge

        return  render(request, 'polls/detailsNeighbor.html', context)
    return HttpResponseRedirect('../../../..')

def warnCharge(request, username, id):
    if request.user.is_authenticated():
        user = Neighbor.objects.get(user=User.objects.get(username=request.user.get_username()))
        neighbor = Neighbor.objects.get(user__username=username)
        if user.type == 'admin' and neighbor.apartment.building == user.apartment.building:
            charge = Charge.objects.get(id=id)
            newWarning = Warning(charge=charge, receiving_neighbor=neighbor)
            newWarning.save()
    return HttpResponseRedirect('/home/neighbors/')

def warnBill(request, username, id):
    if request.user.is_authenticated():
        user = Neighbor.objects.get(user=User.objects.get(username=request.user.get_username()))
        neighbor = Neighbor.objects.get(user__username=username)
        if user.type == 'admin' and neighbor.apartment.building == user.apartment.building:
            bill = Bill.objects.get(id=id)
            newWarning = Warning(bill=bill, receiving_neighbor=neighbor)
            newWarning.save()
    return HttpResponseRedirect('/home/neighbors/')


#financial:
def bankView(request, type, id):
    if type == 'bill':
        bill = Bill.objects.get(id=id)
        if bill.is_payed == True:
            return HttpResponseRedirect('../../../home/financial/bill/')
        if request.method == 'POST':
            form = bankForm(request.POST)
        else:
            form = bankForm()
        if form.is_valid():
            bill.is_payed = True
            bill.payed_date = date.today()
            bill.save()
        return render(request, 'polls/bank.html', {'form': form, 'type' : type})
    else:
        if type == 'charge':
            charge = Charge.objects.get(id=id)
            if charge.is_payed == True:
                return HttpResponseRedirect('../../../home/financial/charge/')
            if request.method == 'POST':
                form = bankForm(request.POST)
            else:
                form = bankForm()
            if form.is_valid():
                charge.is_payed = True
                charge.payed_date = date.today()
                charge.save()
            return render(request, 'polls/bank.html', {'form': form, 'type' : type})
        else:
            if type == 'tenant':
                tenant = MonthlyPayment.objects.get(id=id)
                if tenant.is_payed == True:
                    return HttpResponseRedirect('../../../home/financial/tenant/')
                if request.method == 'POST':
                    form = bankForm(request.POST)
                else:
                    form = bankForm()
                if form.is_valid():
                    tenant.is_payed = True
                    tenant.payed_date = date.today()
                    tenant.save()
                return render(request, 'polls/bank.html', {'form': form, 'type': type})

def tenant(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.get_username()
        user = User.objects.get(username=username)
        neighbor = Neighbor.objects.all().get(user=user)
        # neighbor = user.user;
        context = {}
        context['user'] = neighbor
        context['date'] = date.today();
        monthlyPayments = {}
        if neighbor.apartment is not None:
            monthlyPayments = MonthlyPayment.objects.filter(apartment=neighbor.apartment).order_by('-due_date')
        context['bills'] = monthlyPayments
        return render(request, 'polls/payBills.html', context)
    return HttpResponseRedirect('/login/')

def payBills(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.get_username()
        user = User.objects.get(username=username)
        neighbor = Neighbor.objects.all().get(user=user)
        # neighbor = user.user;
        context = {}
        context['user'] = neighbor
        context['date'] = date.today();
        bills = {}
        if neighbor.apartment is not None:
            bills = Bill.objects.filter(_apartment=neighbor.apartment).order_by('-due_date')
        context['bills'] = bills
        return render(request, 'polls/payBills.html', context)
    return HttpResponseRedirect('/login/')

def payCharges(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.get_username()
        user = User.objects.get(username=username)
        neighbor = Neighbor.objects.all().get(user=user)
        # neighbor = user.user;
        context = {}
        context['user'] = neighbor
        context['date'] = date.today();
        charges = {}
        if neighbor.apartment is not None:
            charges = Charge.objects.filter(_apartment=neighbor.apartment).order_by('-due_date')
        context['charges'] = charges
        return render(request, 'polls/payCharges.html', context)
    return HttpResponseRedirect('/login/')

def financial(request , id , type):
    print('chtoriiiii', id)
    neighbor = get_object_or_404(Neighbor , pk=id)
    print('salammmmm')
    print(neighbor.neighbor_family_name)
    apartment = neighbor.apartment
    return render(request, 'polls/financial.html', {'type' : type , 'id': id , 'apartment':apartment})

def reservation(request , id , reserve):
    return render(request, 'polls/reservation.html' , {'hasreserve' : reserve , 'id' : id})



def guest(request , id , guest_id):
    return render(request , 'polls/guest.html' , {'id' : id , 'guest_id' : guest_id , 'is_modir':(Neighbor.objects.get(pk=id).type == 'modir')})

def validation(request , id):
    return render(request , 'polls/validation.html' , {'id' : id})

def owner(request):
    context = {}
    if request.user.is_authenticated():
        owner = Neighbor(neighbor_name=request.POST.get('name', False),
                            neighbor_family_name=request.POST.get('family_name', False),
                            national_id=request.POST.get('national_id', False))
        if owner.type == 'owner':
            allPayments = MonthlyPayment.objects.filter(owner=owner)
            context['allPayments'] = allPayments

            if request.method == 'POST':
                if 'sendWarning' in request.POST:
                    warningForm = OwnerWarningForm(request.POST)
                    if warningForm.is_valid():
                        newWarning = WarningLetter(owner=owner, title=warningForm.cleaned_data['title'], text=warningForm.cleaned_data['text'], date=date.today())
                        newWarning.save()

                if 'sendingContract' in request.POST:
                    contractForm = OwnerContractForm(request.POST)
                    if contractForm.is_valid():
                        newContract = MonthlyPayment(price=contractForm.cleaned_data['price'], due_date=contractForm.cleaned_data['due_date'])
                        newContract.apartment = owner.apartment
                        newContract.save()


            contractForm = OwnerContractForm()
            context['ownerContractForm'] = contractForm

            warningForm = OwnerWarningForm()
            context['warningForm'] = warningForm

    return render(request, 'polls/owner.html', context)

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

#facilities:
def facilities(request):#todo
    if request.user.is_authenticated():
        user = Neighbor.objects.get(     user = User.objects.get(      username=request.user.get_username())    )
        context = {}
        context['user'] = user
        allFacilities = Facility.objects.filter(_building=user.apartment.building)
        context['facilities'] = allFacilities
        timess = {}
        for facility in allFacilities:
            temp = Reservation.objects.filter(facility=facility)
            allTimesss = []
            # for i in range(0, temp.__len__()):
            #     allTimesss[i] = temp[i].time
            for t in temp:
                allTimesss.__add__([t.time])
            timess[facility.name] = AvailableTimes.objects.filter(facility___building=user.apartment.building, facility=facility).exclude(
                id__in=allTimesss
            )
        context['timess'] = timess

        myReservations = Reservation.objects.filter(neighbor=user)
        context['myReservations'] = myReservations

        if user.type == 'admin':
            form = AddFacilityForm()
            context['addFacilityForm'] = form

        if request.method == 'POST':
            form = AddFacilityForm(request.POST)
            if form.is_valid():
                facility = Facility(name=request.POST['name'], location=request.POST['location'], _building=user.apartment.building)
                facility.save()
                rawTimes = request.POST['availTimes']
                availTimes = rawTimes.split(';')
                for a in availTimes:
                    day = a.split(':')[0]
                    hour = a.split(':')[1]
                    duration = a.split(':')[2]
                    b = AvailableTimes(day=day, hour=hour, duration=duration, facility=facility)
                    b.save()
                return render(request, 'polls/facility.html', context)

        return render(request, 'polls/facility.html', context)
    return HttpResponseRedirect('../../login/')

def deleteReservations(request, username, name, time):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../../../../../log in")
    neighbor = Neighbor.objects.get( user__username=request.user.get_username() )
    # neighbor = Neighbor.objects.get( user=User.objects.get(username=username) )
    facilName = Facility.objects.get(name=name)
    aTime = AvailableTimes.objects.get(id=time)
    aTime.is_reserved = False
    aTime.save()
    reserve = Reservation.objects.get(neighbor=neighbor, facility=facilName, time=aTime)
    reserve.delete()
    return HttpResponseRedirect("../../../../")

def reserveFacility(request, name, id):
    if request.user.is_authenticated():
        user = Neighbor.objects.get(     user = User.objects.get(      username=request.user.get_username())    )
        facility = Facility.objects.get(  name=name  )
        hour = AvailableTimes.objects.get( id = id )
        hour.is_reserved = True
        hour.save()
        reservationn = Reservation(neighbor=user, facility=facility, time=hour)
        reservationn.save()

        return HttpResponseRedirect('../../')
    return HttpResponseRedirect('../../login/')

def removeFacility(request, name, floor):
    if request.user.is_authenticated():
        # user = Neighbor.objects.get(user=User.objects.get(username=request.user.get_username()))
        user = Neighbor.objects.get(user__username=request.user.get_username())
        if user.type == 'admin':
            facility = Facility.objects.get(name=name, location=floor)
            facility.delete()
    return HttpResponseRedirect('../../../')

