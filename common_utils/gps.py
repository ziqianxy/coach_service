# coding=utf-8
import string

'''
调用高德坐标转换接口
1）  服务协议为GET请求
2）  请求地址：http://restapi.amap.com/v3/assistant/coordinate/convert?parameters
3）  请求参数：
------------------------------------------------------------------------
name       |     meaning      |        detail               | 是否必须
-----------|------------------|-----------------------------|---------
key        | user id          | apply from amap             |   必填
locations  | orig locations   | lon and lat                 |   必填
coordsys   | orig coord       | choice: gps, mapbar, baidu  |   必填
output     | type of output   | choice: json(default), xml  |   可选
------------------------------------------------------------------------
locations:
经度和纬度用”,”分割，经度在前，纬度在后，小数点后不得超过6位。多个坐标点间用”;”进行分隔

URL示例：
http://restapi.amap.com/v3/assistant/coordinate/convert?locations=116.481499,39.990475&coordsys=gps&output=xml&key=您申请的key
'''


# gps --> amap
def gps2amap(tuple_list):
    import requests
    import json

    # to transform from list to demanded str format
    tmp = []
    for item in tuple_list:
        tmp.append('%0.6f,%0.6f' % (item[0], item[1]))
    locations = ';'.join(tmp)

    coord_sys = 'gps'
    output = 'json'
    # to apply a key from amap
    key = '90d1c2f423d02d9d274d679b3c67a3ed'
    url = 'http://restapi.amap.com/v3/assistant/coordinate/convert?' \
          'locations={}&coordsys={}&output={}&key={}'.format(locations, coord_sys, output, key)

    # get json str from html body
    html = requests.get(url).text
    # get str of locations
    loc_str = json.loads(html)['locations']

    # transform str to list
    str_list = loc_str.split(';')
    amap_list = []
    for item in str_list:
        tp = item.split(',')
        amap_list.append([string.atof(tp[0]), string.atof(tp[1])])
    return amap_list


# to test the transform
def test():
    location = [(113.50207, 22.97059), (113.5555207, 22.97059)]
    print gps2amap(location)
