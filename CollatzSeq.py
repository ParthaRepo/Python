def collatz(number):
    if(0 == (number % 2)):
        print(number //2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
try:
    number = int(input())
    result = collatz(number)
    if result!=1:
        collatz(result)
except:
    print("please enter the valid number")

