import json
from django.http import HttpResponse
from common.errors import OK

def render_json(data=None, code=OK):
    '''将结果渲染成一个Json格式的HttpResponse返回'''
    result = {
        'code': code,
        'data': data
    }
    json_result = json.dumps(result, ensure_ascii=False,
                             separators=(',', ':'))  # ensure_ascii=False是不将非ascii码转为ascii码，
                                                     # separators是将分隔符进行缩进将json压缩
    return HttpResponse(json_result)
