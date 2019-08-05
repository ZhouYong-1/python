import urllib.request
import re

url = "https://read.douban.com/provider/all"  #获取url
pat1 = '<div class="name">(.*?)</div>'
pat2 = '<div class="works-num">(.*?)</div>'  #匹配规则
data = urllib.request.urlopen(url).read().decode("utf-8") #读取网页的内容并解码
result1 = re.compile(pat1).findall(data)       #会返回一个列表
result2 = re.compile(pat2).findall(data)       #会返回一个列表
file = open(r"C:\Users\1\Desktop\1.txt", "w", encoding="utf-8")  #这里我定义了一个自己的存储路径，大家可以根据自己的路径修改

a = len(result1)
print(result1[3])
for i in range(a):
    file.write(result1[i])
    file.write('      ')
    file.write(result2[i])
    file.write("\n")    #表示换行


file.close()