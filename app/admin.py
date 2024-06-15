from django.contrib import admin
from app.models import Product,Attribute,Image,AttributeValue,Customer,User
# Register your models here.


admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(Image)
admin.site.register(AttributeValue)
admin.site.register(Customer)
admin.site.register(User)
