from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(ShowTime)
admin.site.register(bookmovie)
admin.site.register(Seat)


class AdminMovie(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(MoviePost, AdminMovie)



# Register your models here.
