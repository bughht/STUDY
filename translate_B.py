#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import string
import time
import hashlib
import json

# init
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
my_appid = 20180705000183121
cyber = "nKqEb4H9_0_zU4LOQn5X"
lower_case = list(string.ascii_lowercase)


def requests_for_dst(word):
    # init salt and final_sign
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    # 区别en,zh构造请求参数
    if list(word)[0] in lower_case:
        paramas = {
            'q': word,
            'from': 'en',
            'to': 'zh',
            'appid': '%s' % my_appid,
            'salt': '%s' % salt,
            'sign': '%s' % final_sign
        }
        my_url = api_url + '?appid=' + str(
            my_appid) + '&q=' + word + '&from=' + 'en' + '&to=' + 'zh' + '&salt=' + salt + '&sign=' + final_sign
    else:
        paramas = {
            'q': word,
            'from': 'zh',
            'to': 'en',
            'appid': '%s' % my_appid,
            'salt': '%s' % salt,
            'sign': '%s' % final_sign
        }
        my_url = api_url + '?appid=' + str(
            my_appid) + '&q=' + word + '&from=' + 'en' + '&to=' + 'zh' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response)
    json_reads = json.loads(content)
    out=json_reads['trans_result'][0]['dst']
    return out

