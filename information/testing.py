
with open("cat.txt", "r") as fobj:
    result = ""
    for i in fobj.readlines():
        result += i
    print(result)