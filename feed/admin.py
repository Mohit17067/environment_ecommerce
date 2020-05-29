from django.contrib import admin
from .models import service, bidders, donators, feedback_mosquitokilling, completion_pondcleaning, completion_treeplantation,completion

# Register your models here.
admin.site.register(service)
admin.site.register(bidders)
admin.site.register(donators)
admin.site.register(feedback_mosquitokilling)
admin.site.register(completion_treeplantation)
admin.site.register(completion_pondcleaning)
admin.site.register(completion)