import string
import random
def code(msg):
    st=msg.split(" ")
    st1=[]
    if(len(msg)>=3):
        for i in st:
            a="".join(random.choices(string.ascii_letters+string.digits,k=3))
            b="".join(random.choices(string.ascii_letters+string.digits,k=3))
            stnew=str(a)+i[1:]+i[0]+str(b)
            st1.append(stnew)
        print("Your MSG After Code:"," ".join(st1))
    else:
        print("Your MSG After Code:",msg[::-1])
def decode(msg):
    st=msg.split(" ")
    st1=[]
    if(len(msg)>=3):
        for i in st:
            i=i[3:-3]
            i=i[-1]+i[:-1]
            st1.append(i)
        print("Your MSG After Decoding:"," ".join(st1))
    else:           
        print("Your MSG After Decoding:",msg[::-1])
msg=input("Enter Your MSG:")
op=input("Enter What To Do - Code/Decode:")
if(op=='code' or op=='CODE' or op=='Code'):
    code(msg)
elif(op=='decode' or op=='DECODE' or op=='Decode'):
    decode(msg)
else:
    print('Plz Enter Correct Operation To Perform')
