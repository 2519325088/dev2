from django.contrib import admin

from .models import World,State

# Register your models here.
class StateInline(admin.StackedInline):
    model = State

    extra = 1


class WorldAdmin(admin.ModelAdmin):
    # 排列
    list_display = ["id","wname","wtime"]
    # 过滤器
    list_filter = ['wname']
    # 搜索
    search_fields = ["id","wname","wtime"]
    # 分页
    list_per_page = 2

    inlines = [StateInline]


class StateAdmin(admin.ModelAdmin):
    # 排列
    list_display = ["id","sname","skill"]
    # 过滤器
    list_filter = ["sname","sgender"]
    # 搜索
    search_fields = ["id","sname"]
    # 分页
    list_per_page = 2






admin.site.register(World,WorldAdmin)
admin.site.register(State,StateAdmin)

