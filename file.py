f=open("G:\\Python机器学习实战\\venv\\Scripts\\1.txt","r")
data = f.read()
print(data)
data = f.readline()

f.close()


data="一起学python"
f=open("G:\\Python机器学习实战\\venv\\Scripts\\2.txt","w")
f.write(data)
f.close
f=open("G:\\Python机器学习实战\\venv\\Scripts\\2.txt","w")
data="周勇"
f.write(data)

#write方法是非追加写入

#“”a+追加写入


data="一起学python"
f=open("G:\\Python机器学习实战\\venv\\Scripts\\2.txt","w")
f.write(data)
f.close
f=open("G:\\Python机器学习实战\\venv\\Scripts\\2.txt","a+")
data="周勇"
f.write(data)

