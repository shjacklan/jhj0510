from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from .models import Jhjlist
from .views import backup_switch, restore_switch

admin.site.site_header = '交换机配置备份系统管理平台'
admin.site.site_title = '交换机配置备份系统后台系统'


class JhjlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'ipaddress', 'pinpai', 'weizhi', 'create_time', 'Status', 'beifen_time')
    list_filter = ('pinpai', 'beifen')
    list_max_show_all = 10
    fields = (('ipaddress', 'weizhi'), ('username', 'password'), ('denglu', 'duankou'), 'pinpai', 'beifen')
    radio_fields = {'denglu': admin.HORIZONTAL}

    date_hierarchy = 'create_time'
    actions_on_top = True

    def backup_switch_action(self, request, queryset):
        success_count = 0
        failure_count = 0

        for obj in queryset:
            response = backup_switch(request, obj.id)
            if response == "备份成功":
                success_count += 1
            else:
                failure_count += 1

        if success_count > 0:
            self.message_user(request, f"成功备份了{success_count}个交换机配置", messages.SUCCESS)
        if failure_count > 0:
            self.message_user(request, f"备份失败了{failure_count}个交换机配置", messages.ERROR)

        return HttpResponseRedirect(request.get_full_path())

    backup_switch_action.short_description = "备份交换机配置"

    def restore_switch_action(self, request, queryset):
        success_count = 0
        failure_count = 0

        for obj in queryset:
            response = restore_switch(request, obj.id)
            if response == "恢复成功":
                success_count += 1
            else:
                failure_count += 1

        if success_count > 0:
            self.message_user(request, f"成功恢复了{success_count}个交换机配置", messages.SUCCESS)
        if failure_count > 0:
            self.message_user(request, f"恢复失败了{failure_count}个交换机配置", messages.ERROR)

        return HttpResponseRedirect(request.get_full_path())

    restore_switch_action.short_description = "恢复交换机配置"

    actions = [backup_switch_action, restore_switch_action]

admin.site.register(Jhjlist, JhjlistAdmin)

