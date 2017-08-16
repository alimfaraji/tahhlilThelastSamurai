from django.contrib import admin
from .models import Neighbor
from .models import Bank
from .models import Apartment
from .models import Building
from .models import Owner
from .models import Receipt
from .models import Facility
from .models import Reservation
from .models import Contract
from .models import Dashboard
from .models import UnAvailableTimes
from .models import Charge
from .models import MonthlyPayment
from .models import Bill
from .models import RequestLetter
from .models import WarningLetter
# Register your models here.

admin.site.register(Neighbor)
admin.site.register(Bank)
admin.site.register(Apartment)
admin.site.register(Building)
admin.site.register(Owner)
admin.site.register(Receipt)
admin.site.register(Facility)
admin.site.register(Reservation)
admin.site.register(Contract)
admin.site.register(Dashboard)
admin.site.register(UnAvailableTimes)
admin.site.register(Charge)
admin.site.register(MonthlyPayment)
admin.site.register(Bill)
admin.site.register(RequestLetter)
admin.site.register(WarningLetter)
