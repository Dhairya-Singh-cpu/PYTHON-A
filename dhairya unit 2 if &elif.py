# IF 
age=20
if age >18:
    print("you aer adult")
#IF-eles 
age=20
if age >18:
    print("you are adult")
else:
    print("you are not adult")
#elif 
age=25
if age<18:
    print("you are a minor")
elif age>=18 and age<65:
    print("you are an adult")
else:
    print("you are a senior citizen")
#nested if
age=25
if age>=18:
    if age>=65:
        print("you are eligible for senior citizen discounts")
    else:
        print("you are an adult")
else:
    print("you are a minor")
# for loop
for i in range(5):
    print(i)
for letter in "pyton":
    print(letter)
#using break and continue:
#break
for i in range(10):
    if i==5:
        break
    print(i)
#continue
for i in range(10):
    if i==5:
        continue
    print(i)
#while loop
    i=0
    while i<5:
        print(i)
        i+=1
#  sum of natural number
n=10
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
    print(f"the sum of the first{n}natural number is {sum}")
#program code 1
    i=1
    while i<=10:
        print(i,end='')
        i+=1
#program code 2
num=15
summation=0
c=1
while c<=num:
    summation=c**2+summation
    c=c+1
    print("the sum of square is:", summation)

    
    
