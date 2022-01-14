from django.contrib import admin
from .models import User, Driver, Order, Client

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Client)
admin.site.register(Order)
