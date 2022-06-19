from django.contrib import admin
from jobs.models import Hydjobs,Banglorejbs,Punejobs
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(Hydjobs,HydjobsAdmin)

class BanglorejbsAdmin(admin.ModelAdmin):
    list_display=['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(Banglorejbs,BanglorejbsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']
admin.site.register(Punejobs,PunejobsAdmin)
