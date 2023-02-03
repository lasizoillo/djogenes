from django.contrib import admin

from admirarchy.toolbox import HierarchicalModelAdmin

from .models import Container, Kind, Item


@admin.register(Container)
class ContainerAdmin(HierarchicalModelAdmin):
    hierarchy = True


@admin.register(Kind)
class KindAdmin(HierarchicalModelAdmin):
    hierarchy = True

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass