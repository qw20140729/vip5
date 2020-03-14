
import requests,json

# urlstr = 'http://httpbin.org/post'
#
# payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
#
# payload = json.dumps(payload)
#
# r = requests.post(url=urlstr,data=payload)
#
# print(r.text)
# print(r.json())

# urlstr = 'https://www.wanandroid.com/user/login'
#
# header = {'User-Agent':'Mozilla/5.0'}
# payload = {'username':'qyanls','password':'123456'}
#
# r = requests.post(url=urlstr,data=payload,headers=header)
# # r = requests.post(url=urlstr,data=payload)
#
# print(r.text)
# print(r.headers)

urlstr = 'https://www.wanandroid.com/user/login'
payload = {'username':'qyanls','password':'123456'}

s = requests.session()
r = s.post(url=urlstr,data=payload)
r2 = s.get("https://www.wanandroid.com/lg/todo/list/0")

print(r2.text)
# print(r2.status_code)
print('- '*20)
print(r.text)



