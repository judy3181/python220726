# DemoLoop.py
# 초기값
value = 5
while value > 0:
    print(value)
    value -= 1
    # value = value -1

print("---반복구문---")
lst = ["apple", 100,3.14]
for item in lst:
    print(item,type(item))

d={"apple":100, "orange":200, "banana":300}
for k,v in d.items():
        print(k,v)

#디버깅 모드로 실행할 때 일단 멈춤(Break point : 한땀한땀 살펴본다는 의미)
for i in [2,3,4,5,6]:
    #서식을 지정해서 변경하는 문자
    print("--{0}단--".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0}*{1}={2}".format(i,j,i*j))

print("---break구문---")

lst =[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    #다중 라인 주석처리:ctrl+/
    if item>5:
        break
    print("item:{0}".format(item))
    
print("---continue구문---")

lst =[1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item % 2 == 0:
        continue
    print("item:{0}".format(item))

# 수열: 규칙이 있는 숫자의 열
print(list(range(5)))
print(list(range(1,11)))
print(list(range(2000,2023)))
#range(start,end,step)
print(list(range(10,0,-1)))

print("---리스트 컴프리헨션---")
lst = list(range(1,11))
print(lst)
result = [i**2 for i in lst if i >5]
print(result)

tp= ("apple","kiwi","orange")
print([len(i) for i in tp])
