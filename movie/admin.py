from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(ShowTime)
admin.site.register(BookMovie)
admin.site.register(Seat)
admin.site.register(Room)
admin.site.register(Customer)

class AdminMovie(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(MoviePost, AdminMovie)
