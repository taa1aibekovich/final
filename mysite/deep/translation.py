from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Faculty)
class ProductTranslationOptions(TranslationOptions):
    fields = ('faculty_name', 'description')


@register(Professor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Office)
class ProductTranslationOptions(TranslationOptions):
    fields = ('building', )


@register(Homework)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description', 'title')


@register(Delivery)
class ProductTranslationOptions(TranslationOptions):
    fields = ('feedback', )
