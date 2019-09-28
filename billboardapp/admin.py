from django.contrib import admin
from billboardapp.models import User, Product


admin.site.register(Product)
admin.site.register(User)