import requests
# 这与之前的 urllib.request 不是同一个包

'''案例1'''
'''例1'''
# url ='https://www.sogou.com/web?query=周杰伦'

# resp = requests.get(url)
#
# print(resp.text)

''' 当我们使用以上方式爬取网络中的资源时
    在服务器服务器端会进行反爬，检测到我
    们不是正常的网页浏览，而是通过自动程
    序发起的，这被服务器判定为了不正常行
    为，所以访问出错了
'''

'''例2'''
# url ='https://www.sogou.com/web?query=周杰伦'

# User_agent ={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
# }

# resp2 = requests.get(url,headers=User_agent) # 实现了一个反爬
# 这里简述一下实现原理
# 当我们在网页进行浏览时，协议的请求头中包含了User-agent
# User-agent是请求载体的身份标识，所以当我们使用网页进行
# 浏览时，服务器检测到我们的身份是正常的
# 当我们使用爬虫时，我们手动添加请求头的身份标识，服务器
# 就能正常识别
# print(resp2.text)


'''例3'''
# 我们希望这个爬虫程序更加灵活
# name = input("请输入一个明星的名字： ")
#
# url = f"https://www.sogou.com/web?query={name}"
#
# User_agent ={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
# }
#
# resp3 = requests.get(url,headers=User_agent)
#
# print(resp3.text)


'''案例2'''
# 百度翻译

# url = "https://fanyi.baidu.com/sug" # 我们通过这个链接就能获得单词的翻译
# # 以上内容信息可通过在浏览器中按F12调出，查找
# # 或者右键选择检查
# # 注意我们在获取sug时，需要切换输入法为英文，这样才能获得sug
#
# ''' 所以根据HTTp协议  我们知道fanyi.baidu.com域名下的sug目录
#     就对应着单词翻译数据库目录
# '''
#
# word = input("请输入要翻译的英文单词: ")
#
# data  = {
#     "kw":word
# }
# # 那我们想通过程序的方式实现英文翻译成中文
# # 我们从sug文件中看到，请求方式为POST
# # 所以我们需要调用requests库中的post ：我们在调用requests的库函数要明确请求方式
# resp = requests.post(url,data=data) # 响应为单词翻译
# # 注意POST的传参方式与GET不同
# # GET的传参方式 我们直接将数据放入到了URL地址中
# # 而POST方式是通过body进行传参
#
# # print(resp.text)
# # 输出结果为乱码，因为我们从浏览器中可以看到
# # Content type : application/json 数据格式为json格式
# print(resp.json()) # 所以通过json方法对数据进行反序列化

# 而上面的get方法返回的数据为 text html格式文件，所以不需要json()


'''案例3'''
# 豆瓣电影

# 原网址 https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1
# 问号后面是 参数-
url = "https://movie.douban.com/j/chart/top_list"

param = {
"type": "24",
"interval_id": "100:90",
"action":"",
"start": "0",
"limit": "1"
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
}
resp = requests.get(url,params=param,headers=header)
# get 方法中的params 参数是网址中的查询字符
# data 是需要传输的
resp.encoding='utf-8'
print(resp.content)
print(resp.json())



# 我们查看 requests库 默认的User-agent
# {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

'''如何关闭resp'''
resp.close()
# 记得一定要关闭resp
# 因为每次请求访问，都会建立一个链接，不关闭是默认保持链接的
# 如果多次不关，可能导致后续的访问报错