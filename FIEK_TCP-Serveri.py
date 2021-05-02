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



#-------------METODAT------------
def IPADDRESS():
        HostName = socket.gethostname()
        IP_ADDR = socket.gethostbyname(HostName)
        result = "IP Adresa e klientit eshte: "+str(IP_ADDR) 
        connection.send(result.encode("utf-8"))

def NRPORTIT():
     result = "Klienti eshte duke perdorur portin: "+str(port)
     connection.send(result.encode("utf-8"))

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
    connection.send(result.encode("utf-8"))

def LOJA():
    numbers = []
    for i in range(0,5):
        numbers.append(randint(1,35))
        numbers.sort()
    result=str(numbers)
    connection.send(result.encode("utf-8"))

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
    connection.send(rezultati.encode("utf-8"))
        #8MAGIC_BALL
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
    connection.send(result.encode("utf-8"))



def PERCENTAGE(part, whole):
    p=whole*part/100
    return p

class ClientThread(Thread):
    
    def __init__(self, ip, port,socket):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket=socket
        print("Nje klient eshte lidhur me IP: " + ip + " ne PORT-in: " + str(port))

    def run(self):
        while True:
            try:
                data = connection.recv(128)
            except socket.error:
                print("--------------Ne pritje te kerkesave te klienteve--------------")
                break
            point = data.decode("utf-8")
            points = point.split(' ')
            message1 = points[0]
            message=message1.upper()
            message2=point.replace(message1,"")
            print("Kerkesa e pranuar nga porti  "+str(port) + " : " + point)
            if message == 'finish':
                break
            elif message == "IPADDRESS":
                IPADDRESS()
            elif message == "NRPORTIT":
                NRPORTIT()
            elif message == "NUMERO":
                 result =str(NUMERO(message2))
                 self.socket.send(result.encode("utf-8"))
            elif message == "ANASJELLTAS":
                result =str(ANASJELLTAS(message2))
                self.socket.send(result.encode("utf-8"))
            elif message == "KOHA":
                KOHA()
            elif message == "LOJA":
                LOJA()
            elif message == "PALINDROM":
                result =str(PALINDROM(message2))
                self.socket.send(result.encode("utf-8"))
            elif message == "GCF":
                try:
                    a=int(points[1])
                    b=int(points[2])
                    result=str(GCF(a,b))
                    self.socket.send(result.encode("utf-8"))
                except:
                   result = "Parametrat duhet te jene numera."
                   self.socket.send(result.encode("utf-8"))
            elif message == "KONVERTO":
                try:
                    konverto= points[1]
                    number= int(points[2])
                    if(konverto=="cmNeInch" or konverto=="inchNeCm" or konverto=="kmNeMiles" or konverto=="mileNeKm"):
                        KONVERTO(konverto,number)
                    else:
                        result="Ne ofrojme vetem keto shendrrime: 1.cmNeInch, 2.inchNeCm, 3.kmNeMiles, 4.mileNeKm"
                        self.socket.send(result.encode("utf-8"))
                        continue
                except:
                      result = "Parametrat duhet te jene numera."
                      self.socket.send(result.encode("utf-8"))
           
                
            elif message == "MAGIC":
                MAGIC()
            elif message == "PERCENTAGE":
                  try:
                      part=float(points[1])
                      whole=float(points[2])
                      result=str(PERCENTAGE(part,whole))
                      self.socket.send(result.encode("utf-8"))
                  except:
                      result = "Parametrat duhet te jene numera."
                      self.socket.send(result.encode("utf-8"))


           
            else:
               result="Kerkesa jovalide, shtypni njeren nga kerkesat qe ne ofrojme !!!!"
               self.socket.send(result.encode("utf-8"))

IP_T='127.0.0.1'
PORT_T=14000
TCP_Server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCP_Server.bind((IP_T,PORT_T))

threads = []


print("---------Universiteti i Prishtines \"HASAN PRISHTINA\---------")
print("-----------------------TCP SERVER-----------------------------")
print("\n")

while True:
    print("---------------Serveri po pret per ndonje kerkese--------------------")
    TCP_Server.listen(5)
    (connection, (ip, port)) = TCP_Server.accept()
    newthread = ClientThread(ip, port,connection)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
