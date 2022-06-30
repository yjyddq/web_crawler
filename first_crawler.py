from urllib.request import urlopen

url ="http://www.baidu.com"

resp = urlopen(url) # 打开网址得到响应

# print(resp.read().decode("utf-8"))
# 在 python3 中bytes和str相互转换的方式为
# str = btyes.decode("utf-8")
# bytes = str.encode("utf-8")
# resp.read() 读取到的是网页的源代码 .html 字符编码采用 UTF-8

'''补充'''
# 打印resp.raed() 显示的字符串前有个字符b
# 字符串前加u 表示后面字符串以Unicode格式进行编码
# 字符串前加r 表示屏蔽后面字符串中的转义字符含义，直接原格式输出
# 字符串前加b 表示后面字符串是bytes类型，即采用utf-8编码方式，网络编程、服务器、浏览器中只用bytes格式
# 字符串前加f 表示支持格式化输出
str = resp.read().decode("utf-8")
print(str)


with open("Mybaidu.html",mode="w",encoding='utf-8') as f:
    f.write(str)
    # file.write函数的输入参数需要是str类型
    # 所以，我们需先将byte进行解码decode
    # 然后，写入文件中，注意向文件写入的字符格式为utf-8，Windows系统默认GBK
    # 因为在html文件中我们能看到，字符集采用的编码方式为utf-8，否则中文字符会乱码
print("over!")
