from django.contrib import admin
from django.conf.urls import patterns, url
from . import models


class UnchangeableModelAdmin(admin.ModelAdmin):
    model = models.UnchangeableModel

    def get_urls(self):
        # return the standard urls, except for the change url
        urlpatterns0 = super(UnchangeableModelAdmin, self).get_urls()
        return [p for p in urlpatterns0 if not p.name.endswith("_change")]


admin.site.register(models.UnchangeableModel, UnchangeableModelAdmin)
admin.site.register(models.UnchangeableModelDependency)
