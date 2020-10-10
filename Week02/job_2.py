from fake_useragent import UserAgent
import requests
import time

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://www.processon.com/',
    'path': '/login?f=index'
}


class LoginFailed(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.error_info = ErrorInfo
    def __str__(self):
        return self.error_info


s = requests.Session()
login_url = 'https://www.processon.com/login'
form_data = {
    'login_email': '18500000000',  # 填入有效用户名密码即可登录
    'login_password': '1234567890',
}

# post数据前获取cookie
pre_login = 'https://www.processon.com/login?f=index'
pre_resp = s.get(pre_login, headers=headers)
time.sleep(4)

try:
    response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)
    if '登录失败' in response.text:  # 判断源码中有无登录失败关键字
        raise LoginFailed('登录失败')
    elif '我的文件' in response.text:  # 判断源码中有无我的文件关键字
        print('确认登录成功')
        print('————————————')
except (LoginFailed, Exception) as e:
    print(e)
finally:
    print(f'返回码是: {response.status_code}')  # 打印http服务器返回码
