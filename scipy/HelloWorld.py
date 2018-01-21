#This is the sample program for how statement, loops and conditions works in python.
print("Please enter your name : ")
name = input()
print("Hello ", name)
#This block of code will execute , if the user is partha
if name == 'partha':
    print("Nice to hear back from you. partha!!!")
elif name == 'Partha':
    print("Nice to hear back from you. ", end='')
    print(name)
else:
    print("How are you?")
# for loop
print("Print name 5 time")
for i in range(5):
    print(name)
#While loop
print("Enter the number to test While: ")
number = int(input())
while number<5:
    number = number+1
    print("increment number by one:" ,number)
#Break if name is partha
    if name == 'partha':
        break


