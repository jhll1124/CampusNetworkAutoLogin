import socket
import requests


# 获取本机 IP 地址
ip = socket.gethostbyname(socket.gethostname())

# 设备与帐号等信息
device = "1" # 伪装设备，0 为电脑，1 为手机
account = "1676800"
passwd = "0"
type0 = "cmcc" # cmcc 为移动，telecom 为电信，unicom 为联通，xyw 为教师/临时
mac = '000000000000'

# 构建登录 URL
url = f'http://192.168.200.2:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C{device}%2C{account}%40{type0}&user_password={passwd}&wlan_user_ip={ip}&wlan_user_ipv6=&wlan_user_mac={mac}&wlan_ac_ip=&wlan_ac_name='
print(url, '\n\n', 'Now internal ip is ', ip, '\n', sep='')

# 发送 GET 请求并获取响应
res = requests.get(url).text

if r'\u8ba4\u8bc1\u6210\u529f' in res:
    print('登录成功')
elif r'msg":""' in res:
    print('你已经登录了喵~')
elif 'bGRhcCBhdXRoIGVycm9y' in res:
    print('你他妈密码输错了')
else:
    print(res)
