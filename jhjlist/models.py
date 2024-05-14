from django.db import models

from django.utils.html import format_html
class Jhjlist(models.Model):

    # 交换机品牌，登录协议
    DENGLU = (
        ('0', 'ssh'),
        ('1', 'telnet'),
    )
    BEIFEN = (
        ('0', '未备份'),
        ('1', '已备份'),
    )
    PINPAI = {
        ('0', '锐捷'),
        ('1', '华三'),
        ('2', '华为'),
    }
    # 交换机编号
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # IP地址
    ipaddress = models.GenericIPAddressField(verbose_name='IP地址', protocol='IPv4', db_index=True)
    # 登录账号
    username = models.CharField(max_length=50, verbose_name='登录账号')
    # 登录密码
    password = models.CharField(max_length=50, verbose_name='登录密码')
    # 登录协议
    denglu = models.CharField(max_length=8, choices=DENGLU, verbose_name='登录协议', help_text='必须选择其中一个协议',
                              default=0, db_index=True)
    # 管理端口
    duankou = models.IntegerField(verbose_name='管理端口', default=0)
    # 交换机品牌
    pinpai = models.CharField(max_length=8, choices=PINPAI, verbose_name='交换机品牌', help_text='必须选择其中一个品牌',
                              default=0, db_index=True)
    # 交换机注册时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    # 备份状态
    beifen = models.CharField(max_length=6, choices=BEIFEN, verbose_name='备份状态', default=0, db_index=True)
    # 最后备份时间
    beifen_time = models.DateTimeField(auto_now=True, verbose_name='备份时间')
    #设备位置
    weizhi = models.CharField(max_length=50, verbose_name='设备位置',  default='机房')

    class Meta:

    # 后台管理系统中的名称
        verbose_name = '交换机-列表'



    def __str__(self):
        return self.ipaddress

    def Status(self):

        if self.beifen == '0':
            format_td = format_html('<span style="padding:2px;background-color:red;color:white">未备份</span>')
        elif self.beifen == '1':
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">已备份</span>')
        return format_td
    Status.short_description = "配置备份情况"
