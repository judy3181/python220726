# DemoDict2.py

# phyton에 이름과 전화번호 저장
phone = {"kim":"111", "lee":"222", "park":"333"}
print(phone["kim"])
# in은 단독으로 사용하면 include(멤버십 테스트)
print("park" in phone) #kim씨가 있어?
print("moon" in phone)
print("moon" not in phone)

# 참조를 복사
p = phone
print(p)
print(phone)
print(id(phone), id(p)) #id =identity 민증 느낌

#연산자: >, <, >=, <=. !=(같지않다), ==
#x = 5(입력하라는 의미), 5 == 6(5와 6이 같다?)
print(10>5)
print(10<5)
print(1!=2)
print(1 == 2)

#파이썬의 판단기준
print(bool(0))
print(bool(-3))
print(bool(3))
print(bool(""))
print(bool("demo"))
print(bool([]))
print(bool([1,2,3]))