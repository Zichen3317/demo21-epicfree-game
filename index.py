# -*- coding:utf-8 -*-
# ==========================================
#       Author: ZiChen
#        Mail: 1538185121@qq.com
#         Time: 2021/05/29
#           Version:
#             Description: 执行文件
# ==========================================
import qmsgsent
import epic_freegame
import Win10Inform


def main_handler(event, content):
    data = epic_freegame.GetData('name_endDate')
    name_enddate = ''
    for i in data:
        print(i)
        name_enddate = name_enddate + '%s | 截止：' % i[0] + '%s\n' % i[1]

    message = 'EPIC免费游戏领取：\n%s' % name_enddate
    print(message)
#    qmsgsent.sent('118ebf0721a205155216fdc3095b8c7a', message)
    Win10Inform.Inform(
        './EPIC.ico',
        'EPIC免费游戏领取：',
        name_enddate)


main_handler(1, 2)
