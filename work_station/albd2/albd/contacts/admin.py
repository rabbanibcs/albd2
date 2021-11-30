from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Designation, Contact

@admin.register(Designation)
class DesignationAdmin(ImportExportModelAdmin):
    pass
  
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
  list_display = ['name', 'designation', 'mobile', 'email']
  list_filter = ['designation',]