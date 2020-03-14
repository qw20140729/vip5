import requests

urlstr = 'http://www.baidu.com'
# 调用get方法
result = requests.get(url=urlstr)
print(result.text)
print(result.status_code)


