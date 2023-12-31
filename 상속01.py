#부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name,
             self.phoneNumber))
    

#자식 클래스 정의
class Student(Person):
    #덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 호출(부모 클래스의 것 상속)
        Person.__init__(self,name,phoneNumber)
        #자식 클래스 추가 정의(부모 클래스에 없는 것 정의)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기
        def printInfo(self):
            print("Info(Name:{0}, Phone Number: {1})".format(self.name,
                 self.phoneNumber))
            print("Info(학과:{0}, 학번:{1})".format(self.subject, self.phoneNumber))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201234")
#리턴  값을 dict으로 받는 멤버 변수
print(p.__dict__)
print(s.__dict__)


