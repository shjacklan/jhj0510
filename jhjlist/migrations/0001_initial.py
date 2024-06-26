# Generated by Django 5.0.6 on 2024-05-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jhjlist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="编号"
                    ),
                ),
                (
                    "ipaddress",
                    models.GenericIPAddressField(
                        db_index=True, protocol="IPv4", verbose_name="IP地址"
                    ),
                ),
                ("username", models.CharField(max_length=50, verbose_name="登录账号")),
                ("password", models.CharField(max_length=50, verbose_name="登录密码")),
                (
                    "denglu",
                    models.CharField(
                        choices=[("0", "ssh"), ("1", "telnet")],
                        db_index=True,
                        default=0,
                        help_text="必须选择其中一个协议",
                        max_length=8,
                        verbose_name="登录协议",
                    ),
                ),
                (
                    "pinpai",
                    models.CharField(
                        choices=[("2", "华为"), ("0", "锐捷"), ("1", "华三")],
                        db_index=True,
                        default=0,
                        help_text="必须选择其中一个品牌",
                        max_length=8,
                        verbose_name="交换机品牌",
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="注册时间"),
                ),
            ],
            options={
                "verbose_name_plural": "交换机列表",
            },
        ),
    ]
