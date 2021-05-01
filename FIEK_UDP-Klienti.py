import socket
from socket import *

print("---------------------------------------------------")
name = input("Deshironi ta nderroni emrin e serverit dhe portin?")
if(name== "Po"):
    sName = input("EMRI:")
    sPort=int(input("Porti:"))
else:
    sName= "localhost"
    sPort=14000
print("---------------------------------------------------")
soketiK = socket(AF_INET, SOCK_DGRAM)
soketiK.connect((sName, sPort))
print("--------------------------WELCOME--------------------------")
print("-------------------------TCP-KLIENT-------------------------")

print("\n -------------------------Zgjedhni njeren nga kereksat e me poshtme-------------------------\n")
print("  ---IPADDRESS---\n  ---NRPORTIT---\n  ---NUMERO---\n  ---ANASJELLTAS---\n  ---KOHA---\n  ---LOJA---\n  ---PALINDROM---\n  ---GCF---\n  ---KONVERTO---")
print("Shtyp finish per ndaljen e lidhjes ::: ")

while True:
    request=input("Shtyp njeren nga kerkesat:")
    if request == "finish" or request == "Finish" or request == "FINISH":
        break
    elif(request == "NUMERO" or request == "Numero" or request == "numero"):
      print("Kerkesa duhet te behet ne kete menyre : METODA teksti")
      continue
    elif(request == "ANASJELLTAS" or request == "Anasjelltas" or request == "anasjelltas"):
      print("Kerkesa duhet te behet ne kete menyre : METODA teksti")
      continue
    elif(request == "PALINDROM" or request == "Palindrom" or request == "palindrom"):
      print("Kerkesa duhet te behet ne kete menyre : METODA teksti")
      continue
    elif(request == "GCF" or request == "Gcf" or request == "gcf"):
      print("Kerkesa duhet te behet ne kete menyre : METODA numer1 numer2")
      continue
    elif(request == "KONVERTO" or request == "Konverto" or request == "konverto"):
      print("Kerkesa duhet te behet ne kete menyre : METODA Opsioni numer")
      continue
    elif(request== "PERCENTAGE" or request == "Percentage" or request == "percentage"):
        print("Kerkesa duhet te behet ne kete menyre :METODA x% numer")
        continue
    elif(request == "MAGIC" or request == "Magic" or request == "magic"):
        print("Kerkesa duhet te behet ne kete menyre :METODA pyetja")
        continue
    elif (len(request)>128):
       print("Kerkesa nuk duhet te permbaje mbi 128 karaktere!!!")
       continue
    soketiK.send(request.encode("utf-8"))
    response = soketiK.recv(128)
    print("RESULT ::: " + response.decode("utf-8"))
    print("----------------------------------------------------------------------")

soketiK.close()
