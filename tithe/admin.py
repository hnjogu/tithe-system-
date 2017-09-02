# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib import admin
from .models import Offering

# Register your models here.

@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
	pass
