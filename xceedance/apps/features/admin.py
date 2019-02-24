from django.contrib import admin
from features.models import Feature, Client, TargetVersion
# Register your models here.


class FeatureAdmin(admin.ModelAdmin):
    pass



class ClientAdmin(admin.ModelAdmin):
    pass

class TargetVersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feature, FeatureAdmin)
admin.site.register(Client, ClientAdmin)

admin.site.register(TargetVersion, TargetVersionAdmin)
