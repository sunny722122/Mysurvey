from django.contrib import admin
from .models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=("id","question")

class OptionAdmin(admin.ModelAdmin):
    list_display=("id","option","check")


admin.site.register(Question,QuestionAdmin)
admin.site.register(Option,OptionAdmin)
admin.site.register(Result)