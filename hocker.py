
from urllib.request import urlopen as response
print('''
██   ██  ██████   ██████ ██   ██ ███████ ██████  
██   ██ ██    ██ ██      ██  ██  ██      ██   ██ 
███████ ██    ██ ██      █████   █████   ██████  
██   ██ ██    ██ ██      ██  ██  ██      ██   ██ 
██   ██  ██████   ██████ ██   ██ ███████ ██   ██ v1.0 beta
CC_wolf                                                 
                                                ''')
print( " Type '1' to see Geo location ")
print( " Type '2' to see TCP-Port scaner")
print( " Type '3' to see Whois info ")
print( " Type '4' to see DNS lookup info ")
print( " Type '5' to see Subnet lookup info ")
print( " Type '6' to see Pages info ")
print( " Type '7' to see Reverse IP lookup")
print( " Type '8' to see Reverse DNS lookup")
print( " Type '9' to see Http Headers lookup \n")
data=int(input("Type Here : "))

if data==1:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/geoip/?q="+ip)
    iplocation=response(iplocator).read().decode('utf-8')
    print("\n"+iplocation)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save==save:
        f=open("iplocation.txt","w+")
        f.write(iplocation)
elif data==2:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/nmap/?q="+ip)
    tcpport=response(iplocator).read().decode('utf-8')
    print("\n"+tcpport)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("tcpport.txt","w+")
        f.write(tcpport)
        
elif data==3:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/whois/?q="+ip)
    grabdata=response(iplocator).read().decode('utf-8')
    print("\n"+grabdata)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("whois.txt","w+")
        f.write(grabdata)
        
        
elif data==4:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/dnslookup/?q="+ip)
    grabdata=response(iplocator).read().decode('utf-8')
    print("\n"+grabdata)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("dns.txt","w+")
        f.write(grabdata)

elif data==5:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/subnetcalc/?q="+ip)
    grabdata=response(iplocator).read().decode('utf-8')
    print("\n"+grabdata)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("subnet.txt","w+")
        f.write(grabdata)
elif data==6:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/pagelinks/?q="+ip)
    grabdata=response(iplocator).read().decode('utf-8')
    print("\n"+grabdata)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("pages.txt","w+")
        f.write(grabdata)
elif data==7:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/reverseiplookup/?q="+ip+"&page=2")
    grabdata=response(iplocator).read().decode('utf-8')
    print("\n"+grabdata)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("ReverseIP.txt","w+")
        f.write(grabdata)

elif data==8:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/reversedns/?q="+ip+"&page=2")
    grabdata=response(iplocator).read().decode('utf-8')
    print("\n"+grabdata)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("ReverseDNS.txt","w+")
        f.write(grabdata)

elif data==9:
    ip=input("Type Your Ip or URL: ")
    iplocator= ("https://api.hackertarget.com/httpheaders/?q=http://"+ip)
    grabdata=response(iplocator).read().decode('utf-8')
    print("\n"+grabdata)
    print("Type 'save' to save informations")
    save=input()
    save=save.lower()
    if save.lower()==save:
        f=open("HttpHeader.txt","w+")
        f.write(grabdata)



