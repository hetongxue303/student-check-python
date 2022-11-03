import json
import re
from urllib import request
from ipaddress import ip_address

from exception.custom_exception import IpErrorException


def verify_ip(ip):
    """ 验证ip格式是否正确 """
    try:
        return str(ip_address(ip))
    except Exception as e:
        raise IpErrorException(f'错误的IP格式！ -- {e}')


def by_ip_get_address(ip) -> str:
    """ 根据ip获取地址 """
    verify_ip(ip)

    req = request.Request(f"https://whois.pconline.com.cn/ipJson.jsp?json=true&ip={ip}")
    response = request.urlopen(req).read().decode('gbk')  # 获取响应

    response_dict = json.loads(response)

    if response_dict["proCode"] == "999999":
        return '广东省广州市'
    else:
        return response_dict["pro"] + response_dict["city"]
