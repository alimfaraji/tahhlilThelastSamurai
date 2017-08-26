from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

#
# class Salam(models.Model):
#     esm = models.CharField(max_length=20 , primary_key=True)

class Building(models.Model):
    postal_code = models.CharField(max_length=10 , primary_key=True)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    number = models.IntegerField()


class Apartment(models.Model):
    id = models.IntegerField(primary_key=True)
    building = models.ForeignKey('Building' , on_delete=models.CASCADE , null=True)
    floor = models.IntegerField()
    #_owner = models.ForeignKey('Owner' , on_delete=models.CASCADE , null=True)
    #main_neighbor = models.ForeignKey('Neighbor' , on_delete=models.CASCADE , null=True)

    class Meta:
        unique_together = ('building' , 'floor')

class Neighbor(models.Model):
    user = models.ForeignKey(User, unique=True)
    national_id = models.CharField(max_length=10, primary_key=True, null=False, default='1111')
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, default=0, null=True)
    sex = models.CharField(max_length=5, null=True)
    type = models.CharField(max_length=30, null=True)
    bank_account = models.CharField(max_length=30, null=True)
    _bank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True)
    # isVerified = models.BooleanField(default=False)

class Bank(models.Model):
    name = models.CharField(primary_key=True , max_length=20)


# class Receipt(models.Model):
#     receipt_number = models.IntegerField()
#     _bank = models.ForeignKey('Bank' , on_delete=models.CASCADE)
#     price = models.IntegerField()
#     date = models.DateField()
#
#     class Meta:
#         unique_together = ('receipt_number' , '_bank')

class Facility(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    _building = models.ForeignKey('Building' , on_delete=models.CASCADE , null=True, blank=True)

    class Meta:
        unique_together = ('name' , '_building')


class Reservation(models.Model):
    neighbor = models.ForeignKey('Neighbor' , on_delete=models.CASCADE)
    facility = models.ForeignKey('Facility' , on_delete=models.CASCADE)
    time = models.ForeignKey('AvailableTimes', on_delete=models.CASCADE, default=1)
    #duration = models.IntegerField(default=1)
    #date_time = models.DateTimeField('date of reservation')

    class Meta:
        unique_together = ('neighbor' , 'facility', 'time')

# class Contract(models.Model):
#     _owner = models.ForeignKey('Owner' , on_delete=models.CASCADE)
#     tenant = models.ForeignKey('Neighbor' , on_delete=models.CASCADE)
#     _apartment = models.ForeignKey('Apartment' , on_delete=models.CASCADE)
#     payement_date = models.DateField('date for payement')
#     payement = models.IntegerField(default=1000000)
#     backup_payement = models.IntegerField(default=4000000)
#
#     class Meta:
#         unique_together = ('_owner' , 'tenant' , '_apartment')

class Dashboard(models.Model):
    id = models.IntegerField(primary_key=True)
    _building = models.ForeignKey('Building' , on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField('notification date', null=True, blank=True)
    title = models.CharField(max_length=30, null=True)
    text = models.TextField(null=True)

    class Meta:
        unique_together = ('_building' , 'date_time')

class AvailableTimes(models.Model):
    id = models.IntegerField(primary_key=True)
    facility = models.ForeignKey('Facility' , on_delete=models.CASCADE)
    day = models.IntegerField(default=1)
    hour = models.IntegerField(default=1)
    duration = models.IntegerField(default=1)
    #date_time = models.DateTimeField('available times')

class Charge(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=300000)
    due_date = models.DateField('charge due date')
    payed_date = models.DateField(null=True, blank=True)
    is_payed = models.BooleanField(default=False)
    # receipt = models.ForeignKey('Receipt' , on_delete=models.CASCADE , null=True, blank=True)
    _apartment = models.ForeignKey('Apartment' , on_delete=models.CASCADE)


    class Meta:
        unique_together = ('due_date' , '_apartment')


class MonthlyPayment(models.Model):
    # tenant = models.ForeignKey('Neighbor' , on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey('Neighbor' , on_delete=models.CASCADE, null=True, blank=True)
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField('date of payment')
    price = models.IntegerField(default=2000000)
    is_payed = models.BooleanField(default=False)
    delay_time = models.IntegerField(default=0)
    payed_date = models.IntegerField(null=True, blank=True)

class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=300000)
    due_date = models.DateField('charge due date')
    payed_date = models.DateField(null=True, blank=True)
    is_payed = models.BooleanField(default=False)
    # receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE,blank=True, null=True)
    _apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('due_date', '_apartment')


class RequestLetter(models.Model):
    sender = models.ForeignKey('Neighbor' , related_name='polls_RequestLetter_related' ,
                               related_query_name='polls_RequestLetters')
    date_time = models.DateTimeField(null=True, blank=True)
    receiver = models.ForeignKey('Neighbor' , default=0)
    #number = models.IntegerField(default=1)
    title = models.CharField(max_length=30 , default='')
    type = models.CharField(max_length=30)
    text = models.TextField()


#not used
class WarningLetter(models.Model):
    # receiving_neighbor = models.ForeignKey('Neighbor', on_delete=models.CASCADE, null=True, blank= True)
    owner = models.ForeignKey('Neighbor', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(default="bad neighbor", max_length=300)
    text = models.CharField(max_length=30000)
    date = models.DateField(null=True, blank=True)


class Warning(models.Model):
    receiving_neighbor = models.ForeignKey('Neighbor', on_delete=models.CASCADE)
    charge = models.ForeignKey('Charge', on_delete=models.CASCADE, null=True, blank=True)
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE, null=True, blank=True)

#class ApartmentForm(ModelForm):
#    class Meta:
#        model = Apartment
#        fields = ['number' , 'floor_num']

# class Neighbor(models.Model):
#     national_id = models.CharField(max_length=10 , primary_key=True , null=False , default='1111')
#     neighbor_name = models.CharField(max_length=100)
#     neighbor_family_name = models.CharField(max_length=100)
#     apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE , default=0 , null=True)
#     username = models.CharField(max_length=30 , default='Untitiled')
#     password = models.CharField(max_length=30 , default='123456')
#     sex = models.CharField(max_length=5 , null=True)
#     email = models.CharField(max_length=30 , null=True)
#     type = models.CharField(max_length=30 , null=True)
#     bank_account = models.CharField(max_length=30 , null=True)
#     _bank = models.ForeignKey('Bank' , on_delete=models.CASCADE , null=True)
