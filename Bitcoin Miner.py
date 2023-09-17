#https://github.com/0verTube/Fake-miner-BTC-tiktok

import random
import string
import time
from os import *
from colorama import *

def clear():
    system("cls" if name == 'nt' else "clear")

if name == 'nt':
    system("Bitcoin miner & mode 100, 42")

bitcoin ='''                 ,.=ctE55ttt553tzs.,                               
             ,,c5;z==!!::::  .::7:==it3>.,                         
          ,xC;z!::::::    ::::::::::::!=c33x,                      
        ,czz!:::::  ::;;..===:..:::   ::::!ct3.                    
      ,C;/.:: :  ;=c!:::::::::::::::..      !tt3.                  
     /z/.:   :;z!:::::J  :E3.  E:::::::..     !ct3.                
   ,E;F   ::;t::::::::J  :E3.  E::.     ::.     \ltL               
  ;E7.    :c::::F******   **.  *==c;..    ::     Jttk              
 .EJ.    ;::::::L                   "\:.   ::.    Jttl             
 [:.    :::::::::773.    JE773zs.     I:. ::::.    It3L            
;:[     L:::::::::::L    |t::!::J     |::::::::    :Et3            
[:L    !::::::::::::L    |t::;z2F    .Et:::.:::.  ::[13    
E:.    !::::::::::::L               =Et::::::::!  ::|13       
E:.    (::::::::::::L    .......       \:::::::!  ::|i3       
[:L    !::::      ::L    |3t::::!3.     ]::::::.  ::[13        
!:(     .:::::    ::L    |t::::::3L     |:::::; ::::EE3      
 E3.    :::::::::;z5.    Jz;;;z=F.     :E:::::.::::II3[            
 Jt1.    :::::::[                    ;z5::::;.::::;3t3             
  \z1.::::::::::l......   ..   ;.=ct5::::::/.::::;Et3L             
   \l3.:::::::::::::::J  :E3.  Et::::::::;!:::::;5E3L              
    "cz\.:::::::::::::J   E3.  E:::::::z!     ;Zz37`               
      \z3.       ::;:::::::::::::::;='      ./355F                 
        \z3x.         ::~======='         ,c253F                   
          "tz3=.                      ..c5t32^                     
             "=zz3==...         ...=t3z13P^                        
                 `*=zjzczIIII3zzztE3>*^`                           
'''

print(Fore.YELLOW + bitcoin)
wallet = input("\n\n Wallet ->")
print("https://discord.gg/gfcmKeCrhh JOIN FOR MORE")

print("checking Wallet...")
time.sleep(1.2)

print("Wallet found !")

def id_gen(size=64,chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def id_gen1(size=60,chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

for i in range(1):
    btc = random.uniform(0,2.3)

fake = 0

while(True):
    if(fake > random.randint(10000000000000000,100000000000000000000000000000)):
        print(Fore.LIGHTGREEN_EX + "|  Valid  |" + Fore.LIGHTCYAN_EX +"[-] 0000" + id_gen1() +  Fore.YELLOW + str(btc)+" BTC")
        print("withdrawing to your wallet...")
        time.sleep(5)
        fake = 0
        print("done")
        input("Press any key")
        time.sleep(1)
    else:
        print(Fore.LIGHTRED_EX +"| Invalid |" +Fore.LIGHTCYAN_EX + "[-] "+ id_gen()+Fore.YELLOW +"0.000000000000000 BTC")
        fake +=1 