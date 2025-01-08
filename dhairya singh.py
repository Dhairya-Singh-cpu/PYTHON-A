# len()
a="python is easy to learn"
print(len(a))
# lower()
b="PYTHON IS THE IMPORTANT FOR PROGRAMNER"
print(b.lower())
#Upper()
c="python is good"
print(c.upper())
#REPLACE
d="python is developed in 1991"
str1=d.replace("python","java")
print(d)
print(str1)
#join()
e=('aman','naman','raman','daman')
str1='-'.join(e)
print(str1)
#split()
f="aman-naman-raman-daman"
str1=f.split(' ')
print(str1)
#find()
g="python is a programming language"
str1=g.find("p")
print(str1)
#index()
h="python is a programming language"
str1=h.index("is")
print(str1)
#isalnum()
i="python 1365"
print(i.isalnum())
#isdidit()
j="12345"
print(j.isdigit())
#isnumeric()
k="123456"
print(k.isnumeric())
#islower()
l="python"
print(l.islower())
#isupper
m="PYTHON"
print(m.isupper())



#PYTHON TUPLE:--
t1=()
print(t1)
t2=(10,12,30,40,60)
print(t2)
t3=("c","abc","java")
print(t3)
t4=(501,"python",19.5)
print(t4)
t5=(90,)
print(t5)

#tuple operater
num=(1,2,3,4,5,6)
lang=('python','c','java','php')
print(num+lang)
print(num*2)
print(lang[2])
print(lang[1:4])
print('php'in lang)
print(6 not in num)
#tuple function
#len()
num=(1,2,3,4,5,6)
print("length of tuple:",len(num))
#max()
num=(1,2,3,4,5,6)
lang=('java','c','python','php')
print("max of tuple:",max(num))
print("max of tuple:",max(lang))
#min()
num=(1,2,3,4,5,6)
lang=('java','c','python','php')
print("min of tuple:",min(num))
print("min of tuple:",min(lang))
#sum()
num=(1,2,3,4,5,6)
print("sum of tuple items:",sum(num))
#sorted()
num=(1,2,3,4,5,6)
lang=('java','c','python','php')
print(sorted(num))
print(sorted(lang))
print(sorted(num,reverse=True))
#tuple(sequce)
str="python"
tuple1=tuple(str)
print(tuple1)
num=[1,2,3,4,5,6]
tuple2=tuple(num)
print(tuple2)
#count()
num=(1,2,3,4,3,2,2,1,3,4,5,7)
cnt=num.count(2)
print("count of 2 is:",cnt)
cnt=num.count(10)
print("count of 10 is:",cnt)
#index()
lang=['p','y','t','h','o','n','p','r','o','g','r','a','m']

print("index of t is:",lang.index('t'))
print("index of p is:",lang.index('p'))
print("index of p is:",lang.index('p',3,10))
# python list()
l1=[]
l2=[1,2,3,"python 3.7"]
l3=[1,2,3,4,5]
l4=["python","java","php","language"]
print(l1)
print(l2)
print(l3)
print(l4)
#pyhon list operater
num=[1,2,3,4,5]
lang=['python','c','java','php']
print(num+lang)
print(num*2)
print(lang[2])
print(lang[1:4])
print('cpp' in lang)
print(6 not in num)
#how to delete or remove element
num=[1,2,3,4,5]
print(num)
del num[1]
print(num)
del num [1:3]
print(num)
                                                                                                                          
