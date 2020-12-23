from django.contrib import admin
from .models import FontFamily
from .models import Font


# Register your models here.
admin.site.register(FontFamily)
admin.site.register(Font)
