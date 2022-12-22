from django.contrib import admin
from . import models;
class studentadmini(admin.ModelAdmin):
    list_display=['id','name','phn']
class Teacheradmin(admin.ModelAdmin):
    list_display=['name','exp','subject','contact']
# Register your models here.
admin.site.register(models.student,studentadmini)
admin.site.register(models.Teacher,Teacheradmin)