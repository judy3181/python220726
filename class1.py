# class1.py

#1. 클래스 형식을 정의
class Person:
    #클래스 멤버 변수(클래스 자체에 추가-주로 데이터 공유)

    #초기화 매서드
    def __init__(self):
        self.name = "default name"
        Person.num_person
    #인스턴스 매서드
    def print(self):
        print("My name is {0}".format(self.name))

#내어쓰기(shitf+Tab), 들여쓰기(Tab)
#2. 인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = '전우치'
#3. 매서드 호출
p1.print()
p2.print()
