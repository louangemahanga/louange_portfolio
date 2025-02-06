from django.contrib import admin
from .models import *
# Register your models here.
 

class AdminCustomer(admin.ModelAdmin):
    list_dispaly = ('name', 'email', 'phone', 'address', 'age', 'sex', 'city', 'zip_code')
    
class AdminInvoice(admin.ModelAdmin):
    list_dispaly = ('customer', 'save_by', 'invoice_date_time', 'total', 'last_update_date', 'paid','invoice_ type')
    
admin.site.register(Customer, AdminCustomer)  
admin.site.register(Invoice, AdminInvoice)
admin.site.register(articles)
  
