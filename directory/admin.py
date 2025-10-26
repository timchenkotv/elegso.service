from django.contrib import admin
from .models import Counterparty

@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    list_display = ('counterparty_id','code','display_name','type','country_profile','status','is_deleted')
    list_filter = ('type','country_profile','status','is_deleted')
    search_fields = ('display_name','legal_name','short_name','code')
