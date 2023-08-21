#DemoStrList.py
#디버깅 없이 실행 =Ctrl + F5 (터미널로 실행)
strA = "python is very powerful"
strB = "파이썬은 강력해"
strC = """파이썬을
오늘부터
학습합니다."""

print(strA)
print(len(strB))
print(strC)

result = "py" + "thon"
print(result)

#슬라이싱(인덱싱)
print(strA[0])
print(strA[0:6])

#약식(축약)
print(strA[:6])
print(strA[-3:])

print("--list형식---")
lst = [1,2,3,4,5]
print(len(lst))
#lst 추가
lst.append(10)
lst.insert(1,20)
print(lst)
colors = ["red","blue","green"]
colors += ["red"]
colors +="red"
print(colors)
#lst 제거
colors.remove("red")
print(colors)
#디버깅 할 때 중단점(Break point)
for item in colors:
    print(item)

print("---tuple---")
tp = (10,20,30)
print(len(tp))
print(tp)
print("id:%s, name:%s" %("김","유신"))

#함수 정의
def times(a,b):
    return a+b, a*b

#함수 호출
print(times(5,6))

args = (3,4)
print(times(*args))

#형식 변환
print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c=tuple(b)
print(b)

print("---set---")
a = {1,2,3,3}
b = {3,4,4,5}
print(len(a))
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
