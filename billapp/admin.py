from django.contrib import admin
from .models import billone,billper,billcal,part, ElectricProduct, PlumbingProduct, HardwareProduct,Billing,MyModel,mytiger,partper
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin
admin.site.register(Billing)

admin.site.register(billcal)

admin.site.register(billone)
admin.site.register(billper)
admin.site.register(part)
admin.site.register(partper)
admin.site.register(MyModel)
admin.site.register(mytiger)

@admin.register(ElectricProduct,PlumbingProduct, HardwareProduct)
class ViewAdmin(ImportExportActionModelAdmin):
    pass



























