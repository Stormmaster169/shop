# django-summernote
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from django.contrib import admin


class PrivacyPolicyAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in PrivacyPolicy._meta.fields]

    class Meta:
        model = PrivacyPolicy


admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
