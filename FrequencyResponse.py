import math
import cmath
import re
def main():
    #get user to input resistance since computer is hard to take pictures 
    Zin = input("What is the Z of the input: ")
    ZinFlag = False 
    #if j and omega in Zin, multiply by "jw" to dem of transfer, and remove characters
    if ("jw" in Zin):
        ZinFlag = True
        Zin = Zin.replace("jw", "") 
        #print (Zin) 
    if (("/" in Zin) and (ZinFlag == True)): 
        numIn, denIn = Zin.split('/')
        #print (numIn, denIn)
    else:
        numIn = Zin
        denIn = 1
        #print (numIn, denIn)

    #if j and omega in feed, add "jw" to num of transfer, and remove characters
    feed = input("What is the Z of the feedback: ")
    feedFlag = False
    if ("jw" in feed):
        feedFlag = True
        feed = feed.replace("jw", "") 
    if (("/" in feed) and (feedFlag == True)):
        numFeed, denFeed = feed.split('/')
        print (numFeed, denFeed)
    else:
        numFeed = feed
        denFeed = 1

    #topology determines reponse 
    inv = input ("Is it inverting or noninverting: ")
    transfer = 0 

    #Transfer depends on type of op-amp set up
    if (inv ==  "inv"): 
        transfer = (int(numFeed)*int(numIn)/(int(denIn)*int(denFeed)))*-1
        if (ZinFlag == True):
            transfer = str(transfer) + ("* 1/jw")
        if (feedFlag == True):
            transfer = str(transfer) + ("* jw") 
        #turn into string and cat
        #find - 3dB; 1/2*pi*R*C
        R = int(input("What is R: "))
        C = int (input("What is C: "))
        fc = 1/(2*math.pi*R*C) 
            #where transfer = 1/squareroot of 2
        
    if (inv == "non"):
        transfer = (int(numFeed)*int(numIn)/(int(denIn)*int(denFeed)))
        if (ZinFlag == True):
            transfer = str(transfer) + ("* 1/jw + 1")
        if (feedFlag == True):
            transfer = str(transfer) + ("* jw + 1")
        R = int(input("What is R:"))
        C = int (input("What is C: "))
        fc = 1/(2*math.pi*R*C) 
        #find - 3dB
            #where transfer = 1/squareroot of 2 

    print ("\nDone!\n")
    print (transfer)
    print ("\n")
    print (fc) 
main() 
