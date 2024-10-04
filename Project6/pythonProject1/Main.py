
Something = input("Write here something> ")
Count = 0

def PrintSomething(variable):
    print(variable)
    return variable


def PrintSomethingProVersion(func):

    def wrapper():
        Action = input("You want to add suffix or prefix to something?> ")
        if Action == ("suffix"):
            suffix = input("Suffix here> ")
            print(func + suffix)
        elif Action == ("prefix"):
            prefix = input("prefix here> ")
            print(prefix + func)
        else:
            print("WRONG!")
        return wrapper
    wrapper()

def PrintSomethingCounterVersion(func):
    def wrapper2(*args):
        global Count
        func(args[0])#PrintSomething
        Count = Count + 1
        print(f"Count: {Count}")
    return wrapper2


#PrintSomethingProVersion(PrintSomething(Something)) #Суфих или префикс
#Counting = PrintSomethingCounterVersion(PrintSomething) #Подсчет
#Counting(Something)   #1
#Counting(Something)   #2
#Counting(Something)   #3





