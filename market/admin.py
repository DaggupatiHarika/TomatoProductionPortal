# market/admin.py
from django.contrib import admin
from .models import State, District, Commodity, Market, Price

admin.site.register(State)
admin.site.register(District)
admin.site.register(Commodity)
admin.site.register(Market)
admin.site.register(Price)
