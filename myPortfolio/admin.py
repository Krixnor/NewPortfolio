from django.contrib import admin
from .models import Message, Education,Skills,Service,Porfolio

# Register your models here.
admin.site.register(Message)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Service)
admin.site.register(Porfolio)