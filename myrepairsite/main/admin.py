from django.contrib import admin

from django.contrib import admin
from .models import RepairService, SellRequest, Product, BlogPost

admin.site.register(RepairService)
admin.site.register(SellRequest)
admin.site.register(Product)
admin.site.register(BlogPost)

