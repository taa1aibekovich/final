from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Faculty,Professor,Course, Office, Homework, Delivery)
class ProductAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
# admin.site.register(Faculty)
# admin.site.register(Professor)
admin.site.register(Student)
# admin.site.register(Course)
# admin.site.register(Office)
admin.site.register(Schedule)
admin.site.register(Record)
# admin.site.register(Homework)
# admin.site.register(Delivery)

