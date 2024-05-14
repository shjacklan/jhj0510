from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Jhjlist
import datetime
import os
from netmiko import ConnectHandler


def backup_switch(request, pk):
    jhjlist = get_object_or_404(Jhjlist, pk=pk)

    device_type = {
        '0': 'ruijie_os',
        '1': 'hp_procurve',
        '2': 'huawei',
    }.get(jhjlist.pinpai, 'ruijie_os')

    command = {
        '0': 'show running-config',
        '1': 'display current-configuration',
        '2': 'display current-configuration',
    }.get(jhjlist.pinpai, 'show running-config')

    try:
        device = {
            'device_type': device_type,
            'host': jhjlist.ipaddress,
            'username': jhjlist.username,
            'password': jhjlist.password,
            'secret': jhjlist.password,
        }

        net_connect = ConnectHandler(**device)
        net_connect.enable()

        output = net_connect.send_command(command)

        backup_dir = 'backups'
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        file_name = f"{datetime.datetime.now().strftime('%Y%m%d')}/{jhjlist.ipaddress}.cfg"
        file_path = os.path.join(backup_dir, file_name)

        with open(file_path, 'w') as file:
            file.write(output)

        jhjlist.beifen = '1'
        jhjlist.beifen_time = datetime.datetime.now()
        jhjlist.save()

        net_connect.disconnect()
        return HttpResponse("备份成功", status=200)

    except Exception as e:
        return HttpResponse(f'备份失败: {e}', status=400)


def restore_switch(request, pk):
    jhjlist = get_object_or_404(Jhjlist, pk=pk)

    device_type = {
        '0': 'ruijie_os',
        '1': 'hp_procurve',
        '2': 'huawei',
    }.get(jhjlist.pinpai, 'ruijie_os')

    try:
        device = {
            'device_type': device_type,
            'host': jhjlist.ipaddress,
            'username': jhjlist.username,
            'password': jhjlist.password,
            'secret': jhjlist.password,
        }

        net_connect = ConnectHandler(**device)
        net_connect.enable()

        backup_dir = 'backups'
        file_name = f"{datetime.datetime.now().strftime('%Y%m%d')}/{jhjlist.ipaddress}.cfg"
        file_path = os.path.join(backup_dir, file_name)

        with open(file_path, 'r') as file:
            config_commands = file.read().splitlines()

        net_connect.send_config_set(config_commands)

        jhjlist.beifen = '1'
        jhjlist.beifen_time = None
        jhjlist.save()

        net_connect.disconnect()
        return HttpResponse("恢复成功", status=200)

    except Exception as e:
        return HttpResponse(f'恢复失败: {e}', status=400)
