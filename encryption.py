#Basic encryption program to confuse people
def encryption(list):
    for i in range(len(list)):
        a=ord(list[i])
        a=a+1
        b=chr(a)
        print(b,end='')

li=input("Enter your messgae ")
encryption(li)
