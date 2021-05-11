
import re
x="my 2 favorite numbers are 19 and 42"
y=re.findall("[0-5]+",x) # Find number until the 5 character
print(y)

y=re.findall("[aEIOU]+",x)
print(y)

x="From: Using the : character"
y=re.findall("^F.+:",x) #prefer longest
print(y)

y=re.findall("^F.+?:",x) # prefer shortest
print(y)

a="From stephen.marquard@uct.ac.za  Sat Jan  5 09:14:16 2008"
y=re.findall("\S+@\S+",a)
print(y)
u=re.findall("^From (\S+@\S+)",a) # PARANTEZ icini aliyor 
print(u)

atpos=a.find("@")
print(atpos)

sppos=a.find(" ",atpos)
print(sppos)

host=a[atpos+1:sppos]
print(host)


data="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

words=data.split()
print("words : ",words)
email=words[1]
print(email)
pieces=email.split("@")
print(pieces[1])

y=re.findall("@([^ ]*)",data) 
# burada @"e kadar bul sonrasi icin islem yap
print(y)

y=re.findall("^From .*@([^ ]*)",data)
print(type(y))
print(y)
sum=0
data=open("data.txt")
lst=list()
for line in data:
    line.rstrip()
    y=re.findall("[0-9]+",line)
    if len(y)!=0:
        for i in y:
            sum=sum+int(i)
    print(y)
print(sum)

print ("--------------Seperate---------------")

#Socket
import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
print(type(mysock))
print(mysock)

print ("--------------Seperate---------------")

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd="GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode())
mysock.close()

print ("--------------Seperate---------------")

print(ord("a")) # shows ascii number

print ("--------------Seperate---------------")
import urllib,urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())

print ("--------------Seperate---------------")
import urllib,urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1 #.get dictionaryde key atamak icin
print(counts)


print ("--------------Seperate---------------")
import urllib,urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen("http://www.dr-chuck.com/page1.htm") # also show html codes
for line in fhand:
    print(line.decode().strip())


print ("--------------Seperate---------------")
print ("--------------Seperate---------------")


