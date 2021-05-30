# -*- coding:utf-8 -*-
# ==========================================
#       Author: ZiChen
#        Mail: 1538185121@qq.com
#         Time: 2021/05/29
#           Version: 1.1
#             Description: EPIC免费游戏API
# ==========================================
from urllib import request
import json
# 用requests库的get()方法简明地获取网页信息


def GetData(Type):
    '''
    Type 需要获取的数据
    '''
    url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=zh-CN&country=HK&allowCountries=HK,CN"  # 请求的url
    headers = {  # 请求的头部
        "origin": "https://www.epicgames.com",
        "referer": "https://www.epicgames.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63",
        "x-requested-with": "XMLHttpRequest"
    }

    req = request.Request(url=url, headers=headers)  # GET无data项
    res = request.urlopen(req)
    res = str(res.read(), encoding='utf-8')  # 将返回的bytes类型转为str类型
    data = json.loads(res)  # 如果是json/dict类型,这一步可以转为dict类型,前提是从str转
    # 返回免费游戏的列表（每个游戏都存于一个字典中）
    if Type == 'Game':  # 获取游戏总数据
        return data.get('data').get('Catalog').get('searchStore').get('elements')
    elif Type == 'name_endDate':  # 获取游戏名+领取截止时间
        dataLst = []
        for i in data.get('data').get('Catalog').get('searchStore').get('elements'):
            try:
                endDate_lst = i.get('promotions').get('promotionalOffers')[0].get(
                    'promotionalOffers')[0].get('endDate').split('T')
                endDate = endDate_lst[0]+' '+endDate_lst[1].split('.')[0]
                Name = i.get('title')
                dataLst.append([Name, endDate])
            except:
                endDate = 'None'
        return dataLst
