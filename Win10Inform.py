from win10toast import ToastNotifier
from time import sleep
toaster = ToastNotifier()


def Inform(icon_path, title, content):
    # 有icon的版本
    toaster.show_toast(title,
                       content,
                       icon_path=icon_path,
                       duration=10)

    # 等待提示框关闭
    while toaster.notification_active():
        sleep(0.1)
