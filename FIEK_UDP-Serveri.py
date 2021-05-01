import socket
import datetime
import math 
from threading import Thread
from socketserver import ThreadingMixIn
from socket import gethostbyaddr
import random
from random import randint
import os
from _thread import *
import sys
import struct

UDP_Port=14000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',UDP_Port))
print("--------------------UDP-SERVER--------------------\n")
def IPADDRESS():
     result="IP Adresa: "+str(addr[0])
     return result

def NRPORTIT():
     result = "Klienti eshte duke perdorur portin: "+str(addr[1])
     return result

def NUMERO(teksti):

    zanore = 0
    bashketingellore = 0
    for letter in teksti:
            if(letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" 
               or letter == "U" or letter == "u" or letter == "Y" or letter == "y"):
                zanore = zanore + 1
            else:
                bashketingellore = bashketingellore + 1
               
    result = "Numri i zanoreve ne tekstin e dhene eshte :::" +str(zanore) + ", ndersa numri i bashketingelloreve eshte :::" + str(bashketingellore-1)
    return result

def ANASJELLTAS(text):
        result = text[::-1]
        return result

def PALINDROM(txt):
    rev_txt = txt[::-1]
    if(rev_txt == txt):
            return "Teksti i dhene eshte PALINDROME"
    else:
            return "Teksti i dhene nuk eshte PALINDROME"

def KOHA():
    now = datetime.datetime.now()
    result = now.strftime("%d.%m.%Y %H:%M:%S %p")
    return result

def LOJA():
    numbers = []
    for i in range(0,5):
        numbers.append(randint(1,35))
        numbers.sort()
    result=str(numbers)
    return result

def GCF(a,b):
    input=int(a)
    input=int(b)
    if(b==0):
        result = a
    else:
        result = GCF(b,a%b)
    return result
def KONVERTO(konverto,number):
    input = float(number)
    result = 0
    if(konverto == "cmNeInch"):
        result = number*2.54
    elif(konverto == "inchNeCm"):
        result = number/2.54
    elif(konverto == "kmNeMiles"):
        result = number/1.609
    elif(konverto == "mileNeKm"):
        result = number*1.609
    rezultati = str("%.2f" % result)
    return rezultati
def MAGIC():
    answers = random.randint(1,8)
    if answers == 1:
       result = "It is certain"
    
    elif answers == 2:
        result =  "Outlook good"
    
    elif answers == 3:
        result =  "You may rely on it"
    
    elif answers == 4:
       result =  "Ask again later"
    
    elif answers == 5:
        result =  "Concentrate and ask again"
    
    elif answers == 6:
       result =  "Reply hazy, try again"
    
    elif answers == 7:
       result =  "My reply is no"
    
    elif answers == 8:
       result =  "My sources say no"
    return result


def PERCENTAGE(part, whole):
    p=whole*part/100
    return p

while True:
     print("------------------Duke pritur per kerkesa te klienteve------------------")
     request,addr =s.recvfrom(1024)
     point= request.decode("utf-8")
     points = point.split(' ')
     message1 = points[0]
     message=message1.upper()
     firstpoint=point.replace(message1,"")

     print("Kerkesa e pranuar:"+point)
     if message =="FINISH":
           break
     elif message == "IPADDRESS":
         s.sendto(str(IPADDRESS()).encode('utf-8') , addr)
     elif message == "NRPORTIT":
         s.sendto(str(NRPORTIT()).encode('utf-8') , addr)
     elif message == "NUMERO":
           result =str(NUMERO(firstpoint))
           s.sendto(result.encode("utf-8"),addr)
     elif message == "ANASJELLTAS":
          result =str(ANASJELLTAS(firstpoint))
          s.sendto(result.encode("utf-8"),addr)
     elif message == "PALINDROM":
          result =str(PALINDROM(firstpoint))
          s.sendto(result.encode("utf-8"),addr)
     elif message == "KOHA":
         s.sendto(str(KOHA()).encode('utf-8') , addr)
     elif message == "LOJA":
         s.sendto(str(LOJA()).encode('utf-8') , addr)
     elif message == "GCF":
                try:
                    a=int(points[1])
                    b=int(points[2])
                    result=str(GCF(a,b))
                    s.sendto(result.encode("utf-8"),addr)
                except:
                       result = "Parametrat duhet te jene numera."
                       s.sendto(result.encode("utf-8"),addr)
     elif message == "KONVERTO":
         try:
                    konverto= points[1]
                    number= int(points[2])
                    if(konverto=="cmNeInch" or konverto=="inchNeCm" or konverto=="kmNeMiles" or konverto=="mileNeKm"):
                        KONVERTO(konverto,number)
                    else:
                        result="Ne ofrojme vetem keto shendrrime: 1.cmNeInch, 2.inchNeCm, 3.kmNeMiles, 4.mileNeKm"
                        s.sendto(result.encode("utf-8"),addr)
                        continue
         except:
                      result = "Parametrat duhet te jene numera."
                      s.sendto(result.encode("utf-8"),addr)
     elif message == "MAGIC":
                s.sendto(str(MAGIC()).encode('utf-8') , addr)
     elif message == "PERCENTAGE":
                 try:
                      part=float(points[1])
                      whole=float(points[2])
                      result=str(PERCENTAGE(part,whole))
                      s.sendto(result.encode("utf-8"),addr)
                 except:
                       result = "Parametrat duhet te jene numera."
                       s.sendto(result.encode("utf-8"),addr)

