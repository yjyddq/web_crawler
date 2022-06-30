import requests
import re
import csv
'''实战1'''
# 用正则表达式提取，从网页上获取的html文件中的数据
'''例1'''
url = "https://movie.douban.com/top250"

headers ={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
}

resp = requests.get(url,headers=headers)
# print(resp.text) # 查看抓取的网页源代码内容
# 返回为JS文件，包含我们需要的数据
'''我们想要获得电影名字、上映时间、评分、参评人数'''

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<people>.*?)人评价</span>.*?</li>',re.S)

result = obj.finditer(resp.text)

# for data in result:
#     print(data.group("name"))
#     print(data.group("year").strip()) # strip是生成器/迭代器类的一个内置方法 去除某一指定的字符  没有指定则去除空格
#     print(data.group("score"))
#     print(data.group("people"))

'''写入文件'''
with open("data250.csv","w") as f:
    csvwriter = csv.writer(f)
    for data in result:
        dict = data.groupdict()
        dict["year"]=dict["year"].strip()
        csvwriter.writerow(dict.values())

resp.close()

# 以上例子我们只抓取到了第一页的数据
# 那么如何抓取其他页的数据呢
# 以下为实现
'''例2'''
# 可以灵活控制读入多少页的内容
# EndPage = input("请输入要抓取多少页数据: ")
#
# headers ={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37"
# }
#
# obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
#                      r'.*?<br>(?P<year>.*?)&nbsp.*?'
#                      r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
#                      r'<span>(?P<people>.*?)人评价</span>.*?</li>',re.S)
#
# for p in range(0,int(EndPage),25):
#
#     url = f"https://movie.douban.com/top250?start={p}&filter="
#
#     resp = requests.get(url,headers=headers)
#
#     result = obj.finditer(resp.text)
#
#     '''写入文件'''
#     with open("movietop250.csv", "a") as f:
#         csvwriter = csv.writer(f)
#         for data in result:
#             dict = data.groupdict()
#             dict["year"] = dict["year"].strip()
#             csvwriter.writerow(dict.values())
#
#     resp.close()


'''实战2'''



