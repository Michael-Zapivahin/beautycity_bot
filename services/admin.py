from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Client,
    Employee,
    Procedure,
    Salon,
    Schedule,
    Payment
)


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    def image_tag(self, employee):
        # return format_html('<img src="{}" />'.format(obj.photo.url))
        return format_html(
            '<img style="max-height:{height}" src="{url}"/>',
            url=employee.photo.url,
            height='100px',
        )

    image_tag.short_description = 'Photo'
    list_display = ['name', 'phone', 'image_tag']


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    pass


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
