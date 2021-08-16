import random
import pyautogui
#Enjoy
alp="abce1234567890@"
alp_list=list(alp)
print(alp_list)

password=  pyautogui.password("Enter a password: ")
guesspassword=""

while(guesspassword!=password):
    guesspassword=random.choices(alp_list, k=len(password))
    print("<===================="+str(guesspassword)+"======================>")

    if(guesspassword== list(password)):
        print("your password is: ",guesspassword)
        break
        
