#demoStr.py
#print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))
result = strA.upper()
print(result)
print(strA.startswith("py"))
print(strA.endswith("ful"))


data = "aaa::bb::cc"
lst = data.split("::")
print(lst)
