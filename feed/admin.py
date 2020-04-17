from django.contrib import admin
from .models import service, bidders, donators

# Register your models here.
admin.site.register(service)
admin.site.register(bidders)
admin.site.register(donators)