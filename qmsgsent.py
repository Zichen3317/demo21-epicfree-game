# author： Zichen
# date: 2021-02-02
#vision: 1.0
# instruction： 利用Qmsg酱发送信息模块

from requests import post as requests_post
import traceback


def sent(qmsgkey, content):
    '''
    用于向qmsg酱发送请求及内容的函数
    参数：
    qmsgkey 
    content 需要发送的内容
    '''
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://qmsg.zendee.cn/send/%s?msg= %s" % (qmsgkey, content)
    try:
        r = requests_post(api_url, headers=headers).content
        print("[Qmsg]已发送√")
    except:
        traceback.print_exc()
