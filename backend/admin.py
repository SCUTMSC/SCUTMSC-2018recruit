from django.contrib import admin

# Register your models here.

from backend.models import Layman, NorthCampus,CC

@admin.register(Layman)
class LaymanAdmin(admin.ModelAdmin):
    list_display = ('name','department1','department2','schoolID','interview','passed')
    list_per_page = 20
    ordering = ('ID',)
    list_editable = ['interview','passed',]

    list_filter = ('department1','department2','interview','passed')
    search_fields = ('schoolID','name',)

@admin.register(NorthCampus)
class NorthCampusAdmin(admin.ModelAdmin):
    list_display = ('name','department1','department2','schoolID','interview','passed')
    list_per_page = 20
    ordering = ('ID',)
    list_editable = ['interview','passed',]

    list_filter = ('department1','department2','interview','passed')
    search_fields = ('schoolID','name',)

@admin.register(CC)
class CCAdmin(admin.ModelAdmin):
    list_display = ('name','sex','schoolID','classes','introduce','passed')
    list_per_page = 20
    ordering = ('ID',)
    list_editable = ['passed',]

    list_filter = ('classes','passed')
    search_fields = ('schoolID','name',)