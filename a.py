print("Welcome to Random Password Generator")
import random
list_capi=[]
list_small=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_special=["!","@","#","$","%","^","&","*","(",")","/","+","-","\"/","]","{}","}","|","~","`","["]
for element in list_small:
    list_capi.append(element.upper())
password=""

for r in range(2):
    r_num=random.randint(1,100)
    ran_capi=random.randint(0,len(list_capi)-1)
    ran_small=random.randint(0,len(list_small)-1)
    
    ran_special=random.randint(0,len(list_special)-1)
    upper=list_capi[ran_capi]
    lower=list_small[ran_small]
    special=list_special[ran_special]
    choice=random.randint(1,4)
    
    password +=upper+lower+special+str(r_num) if choice==1 else  (upper+special+lower+str(r_num)) if choice==2 else (lower+upper+str(r_num)+special) if choice==3 else (special+str(r_num)+upper+lower)
print("Your Random Password")
print(password)

