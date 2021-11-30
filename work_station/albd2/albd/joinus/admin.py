from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Division, District, Constituency, JoinUs
from .forms import JoinUsAdminForm


@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin):
    search_fields = ('name',)


@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ['name', 'division', 'code', 'latitude', 'longitude']
    list_filter = ['division',]
    search_fields = ('name', )


@admin.register(Constituency)
class ConstituencyAdmin(ImportExportModelAdmin):
    list_display = ['name', 'district', 'code']
    list_filter = ['district']
    search_fields = ('name',)


@admin.register(JoinUs)
class JoinUsAdmin(ImportExportModelAdmin):
    form = JoinUsAdminForm
    list_display = ['full_name', 'dob', 'gender', 'mobile', 'email', 'district', 'constituency', 'preference', 'join_date']
    list_filter = ['division', 'district', 'constituency', 'gender']
    search_fields = ('mobile', )
