#class1.py
#1)클래스 형식을 정의
class Person:
    #초기화 메서드
    def __init__(self):
        #인스턴스 멤버 변수 초기화
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()

#3)메서드 호출
p1.name = "전우치"
p1.print()
p2.print()

#런타임(코드가 실행되는 시점) #Person 클래스에 정의되지 않은 name 추가는 좋지 않다.
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스에 추가 # 인스턴스에 추가는 정의되지 않은 name 추가도 좋지 않다. p1만 작동되고, p2는 에러남
p1.age = 30
print(p1.age)
#print(p2.age)
#print(Person.age)

