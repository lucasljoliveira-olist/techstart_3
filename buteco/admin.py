from django.contrib import admin

from buteco.models import Team, Customer, Sport, Product
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'phone')

class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(Team, TeamAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)