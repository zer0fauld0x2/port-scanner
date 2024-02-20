#!/usr/bin/env python3
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Z E R O - F A U L D")
print(""" 
      Port Tarama Aracı - Port Scanner Tool : 
1).Fast Scanner
2).Service and version information
3).Operating System information
      
""")
islem_no = input("Transaction ID : ")
if(islem_no=="1"):
       IPAdress = input("Target IP Adress : ")
       os.system("nmap " +IPAdress)
elif(islem_no=="2"):
       IPAdress = input("Target IP Adress : ")
       os.system("nmap -sS -sV "+ IPAdress)
elif(islem_no=="3"):
      IPAdress=input("Target IP Adress : ")
      os.system("nmap -O"+ IPAdress)
    
print("---Author Zer0Fauld---")