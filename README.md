声明：未经过详细测试，有效性不保证。
用的pycharm,windows11下开发，python 3.10.14
利用django中admin功能增加两个ACTION动作，用netmiko工具包对列表交换机进行备份以及恢复之前的备份。
列表交换机参数保存在sqlite3数据库中，交换机配置保存在backups文件夹中。

<img width="1248" alt="111" src="https://github.com/shjacklan/jhj0510/assets/116077470/f76c899e-1422-4504-b73c-b927dffcf671">

action动作是admin自带的功能，不需要再增加页面啥的，方便，主要代码看jhjlist下admin.py,views.py,models.py以及urls.py。另外根目录下urls.py和settings.py也有修改。

感谢徐老师的脚本。
