#function2.py
#스코핑롤(이름 해석 규칙):LGB 규칙
#전역변수
x = 1
def func(a):
    return a+x

#호출
print(func(1))

def func2(a):
    #지역변수
    x = 5
    return a + x

#호출
print(func2(1))
