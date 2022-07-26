# DemoLoop.py
# 초기값
value = 5
while value > 0:
    print(value)
    value -= 1
    # value = value -1

print("---반복구문---")
list = ["apple", 100,3.14]
for item in list:
    print(item,type(item))

d={"apple":100, "orange":200, "banana":300}
for k,v in d.items():
        print(k,v)

for i in [2,3,4,5,6]:
    #서식을 지정해서 변경하는 문자
    print("--{0}단--".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0}*{1}={2}".format(i,j,i*j))

print("---break구문---")

lst =[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item>5:
        break
    print("item:{0}".format(item))
