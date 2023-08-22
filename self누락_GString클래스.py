#전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그  #self.으로 선언해야한다.(선언하지 않으면 전역변수로 리턴됨)
        print(str)

g = GString()
g.set("First Message")
g.print()
