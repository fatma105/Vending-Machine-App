import threading  
## Defining of a method  
def close():
    if x==0:
        print("Timed out")


def shit():        
    threading.Timer(5,close).start()

shit()
x=0

while True:
    x=input("enter x: ")