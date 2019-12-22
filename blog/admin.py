from django.contrib import admin
from .models import Contact,Giverent_field,sell_car_post, car_choose, User_rent_form
# Register your models here.


admin.site.register(Contact)
admin.site.register(Giverent_field)
admin.site.register(sell_car_post)
admin.site.register(car_choose)
admin.site.register(User_rent_form)
