#demoDict.py

# 사전식구조
color = {"apple":"red","banana":"yellow"}
print(color)
print(len(color))
print(color["apple"])
color["cherry"] = "red"
print(color)

del color['apple']
print(color)
for item in color.items():
    print(item)


print("---key---")
for k in color.keys():
    print(k)

print("---value---")
for v in color.values():
    print(v)

#장비물 관리 : 기기별 개수
device = {"iphone":5, "i-pad":10, "windows":20}
print(device)
print(len(device))
print(device["iphone"])

#입력
device["android"] =30
#삭제
del device["iphone"]
#수정
device["i-apd"] = 11
print(device)

#무조건 파이썬은 참조를 복사해서 전달
device2 = device
device2["macbook"] = 20
print(device)
print(device2)
