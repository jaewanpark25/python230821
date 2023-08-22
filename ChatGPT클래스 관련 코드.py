# 기본 클래스 Person을 정의합니다.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print(f"이름: {self.name}, 나이: {self.age}")


# Person 클래스로부터 상속받는 파생 클래스 Employee를 정의합니다.
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)  # 기본 클래스의 생성자를 호출합니다.
        self.role = role
    
    def printInfo(self):
        super().printInfo()  # 기본 클래스의 printInfo() 메서드를 호출합니다.
        print(f"직책: {self.role}")


# Person 클래스로부터 상속받는 또 다른 파생 클래스 Manager를 정의합니다.
class Manager(Person):
    def __init__(self, name, age, skill):
        super().__init__(name, age)  # 기본 클래스의 생성자를 호출합니다.
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()  # 기본 클래스의 printInfo() 메서드를 호출합니다.
        print(f"기술: {self.skill}")


# Employee와 Manager의 인스턴스를 생성합니다.
employee1 = Employee("John", 30, "개발자")
employee2 = Employee("Jane", 28, "디자이너")
manager1 = Manager("Alice", 40, "리더십")
manager2 = Manager("Bob", 45, "전략가")

# printInfo() 메서드를 사용하여 정보를 출력합니다.
print("직원 1 정보:")
employee1.printInfo()

print("\n직원 2 정보:")
employee2.printInfo()

print("\n매니저 1 정보:")
manager1.printInfo()

print("\n매니저 2 정보:")
manager2.printInfo()

# 상속과 isinstance() 함수를 테스트합니다.
print("\nisinstance() 확인:")
print(isinstance(employee1, Person))  # True
print(isinstance(manager1, Employee))  # False
print(isinstance(manager2, Manager))   # True

# 다중 상속에서 isinstance() 함수를 테스트합니다.
print("\n다중 상속:")
print(isinstance(manager1, Person))    # True
print(isinstance(manager1, Employee))  # True

# 메서드 오버라이딩을 데모합니다.
class NewEmployee(Employee):
    def printInfo(self):
        super().printInfo()  # 기본 클래스의 오버라이딩된 메서드를 호출합니다.
        print("이것은 NewEmployee 클래스입니다.")

print("\nNewEmployee 정보:")
new_employee = NewEmployee("Sam", 25, "새로운 역할")
new_employee.printInfo()
