from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee,Department,Attendance,Kin
from .models import Employees, Muster_wages




class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register([Employee,Department,Attendance,Kin])


admin.site.register(Employees,BlogAdmin)
admin.site.register(Muster_wages,BlogAdmin)
