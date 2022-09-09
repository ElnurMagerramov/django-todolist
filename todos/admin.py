from django.contrib import admin
from .models import MyModel, Todos, Got
# Register your models here.

admin.site.register(Todos)
admin.site.register(Got)
admin.site.register(MyModel)