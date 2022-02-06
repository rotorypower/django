from django.contrib import admin

from homework.models import Homework


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "created_at")
    fields = ("user", "age", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email",)
    raw_id_fields = ("user",)