"""
初始化数据
@Author:何同学
"""
from datetime import datetime, date

accountData = [
    {
        'username': 'admin',
        'password': '$2b$12$I5lfn4eO8M0oH4yYQWjSQ.t4VJz9cGKXA.ht6syIG6tAXmbnQywqa',
        'last_login_time': datetime(2022, 11, 5, 12, 55, 00),
        'last_login_ip': '127.0.0.1',
        'create_time': datetime(2022, 11, 5, 12, 55, 00),
        'update_time': datetime(2022, 11, 5, 12, 55, 00)
    }
]
adminData = [
    {
        'name': '何同学',
        'gender': '1',
        'birthday': date(2000, 3, 3),
        'address': '重庆市'
    }
]
