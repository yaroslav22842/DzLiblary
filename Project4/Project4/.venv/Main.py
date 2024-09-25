

result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
            return a/b
    except NameError:
        print("Incorrect name")
    except TypeError:
        print("Incorrect type")

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
    for key in data:
        res = divider(key, data[kem])
        result.append(res)
        print(result)

except TypeError:
    print("Incorrect data")
except NameError:
    print("Incorrect Name")



