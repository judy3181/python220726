# DemoBool.py

#얕은복사

a = [1,2,3]
#항상 파이썬은 참조만 복사(Pass By Reference)
b = a 
print(a)
print(b)
print(id(a),id(b))

print("---deepcopy---")

a = [1,2,3]
#항상 파이썬은 참조만 복사(Pass By Reference)
b = a[:]
print(a)
print(b)
print(id(a),id(b))

# 다른 형식이라면
import copy 
a = [100,200,300]
b = copy.deepcopy(a)
a[0] = 101
print(a)
print(b)
print(id(a),id(b))