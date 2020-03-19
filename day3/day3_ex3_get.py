import requests

# urlstr = 'http://www.baidu.com'
# # 调用get方法
# result = requests.get(url=urlstr)
# print(result.text)
# print(result.status_code)
# print(result.encoding)

url = 'https://www.wanandroid.com/article/query'
paylod = {'k':'Android'}
r = requests.get(url=url,params=paylod)
print(r.text)
print(r.status_code)
print(r.url)
print(r.cookies)
