name = input('enter a string')
print(name)
print("type ",type(name))
print(len(name))

a = len(name)
print("first letter of name is ",name[-1])
print("strip ",name.strip('*'))
print("left strip", name.lstrip('*'))
print("right strip",name.rstrip('*'))

print("java to change python", name.replace("java","python"))

print("lower casee ",name.islower())
print("lower casee ",name.isupper())

num = int(input("enter your number"))
print(type(num))
