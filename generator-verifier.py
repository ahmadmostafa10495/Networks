def logical_xor(str1, str2):
    return bool(str1) ^ bool(str2)
from operator import xor
def getbool(str1):
    if str1 =="1":
        return True
    if str1 =="0":
        return False

import tkinter as tk

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk


##############################################################################
def gen (message, poly):
    i = 0
    j = 0
    for x in poly:
        i+=1
    orderOfGenerator = i    
    for x in message:
        j+=1
    x = 0    
    while x<j:
        if message[x] == "0" or message[x] == "1":
            x +=1
        else:
            break
    messageBitsBeforeAddingZeros = x    
    while i>1:
        message = message[:x] + '0'
        x+=1
        i-=1
    print (poly)
    print (message)
    toBeCal = ""
    for m in range(orderOfGenerator):
        
        toBeCal += message[m]
    out = ""
    t = 0
    v = []

    message1 = message
    while t<(messageBitsBeforeAddingZeros +orderOfGenerator -1 - orderOfGenerator):
        if toBeCal[0] == '1':
            for m in range(orderOfGenerator):
                v.insert(m,(int(xor(getbool(toBeCal[m]), getbool(poly[m])))))
                           
            ''' v.insert(0,(int(xor(getbool(toBeCal[0]), getbool(poly[0])))))
            v.insert(1,(int(xor(getbool(toBeCal[1]), getbool(poly[1])))))
            v.insert(2,(int(xor(getbool(toBeCal[2]), getbool(poly[2])))))
            v.insert(3,(int(xor(getbool(toBeCal[3]), getbool(poly[3])))))'''
            
            
            if v[0] == 0:
                toBeCal = str(v[1])
                for m in range(orderOfGenerator - 2):
                    toBeCal += str(v[m+2])
                toBeCal += message[t+orderOfGenerator]
                '''if v[1] == 0:
                    toBeCal = str(v[2])+str(v[3])+message[t+4]+message[t+5]
                    if v[2] == 0:
                        toBeCal = str(v[3])+ message[t+4]+message[t+5]+message[t+6]
                        if v[3] == 0:
                            toBeCal = message[t+4]+message[t+5]+message[t+6]+message[t+7]
                        
                '''
                
            
            
        else:
            tempToBeCal = toBeCal
            toBeCal = tempToBeCal[1]
            for m in range(orderOfGenerator - 2):
                    toBeCal += str(tempToBeCal[m+2])
            toBeCal += message[t+orderOfGenerator]
        print(toBeCal)    
        t+=1
        v=[]
    for m in range(orderOfGenerator-1):
        out+=toBeCal[m+1]
    transmitted = message
    x = messageBitsBeforeAddingZeros
    i = orderOfGenerator
    m = 0
    while i>1:
        transmitted = transmitted[:x] + out[m]
        x+=1
        i-=1
        m+=1
    print("transmitted " + transmitted)
    outfile = "transmitted_message.txt"
    fileo = open(outfile, "w")
    fileo.write(transmitted)
    fileo.close()
    root = tk.Tk()
    w = tk.Label(root, text="Transmitted message is: "+transmitted)
    w.pack()
    #root.mainloop()
    return transmitted
##########################################################################
def ver (message, poly):
    i = 0
    j = 0
    for x in poly:
        i+=1
    orderOfGenerator = i    
    for x in message:
        j+=1
    x = 0    
    while x<j:
        if message[x] == "0" or message[x] == "1":
            x +=1
        else:
            break
    messageBitsBeforeAddingZeros = x+1 - orderOfGenerator  
    ''' while i>1:
        message = message[:x] + '0'
        x+=1
        i-=1'''
    print (poly)
    print (message)
    toBeCal = ""
    for m in range(orderOfGenerator):
        
        toBeCal += message[m]
    out = ""
    t = 0
    v = []
    
    message1 = message
    while t<(messageBitsBeforeAddingZeros +orderOfGenerator -1 - orderOfGenerator):
        if toBeCal[0] == '1':
            for m in range(orderOfGenerator):
                v.insert(m,(int(xor(getbool(toBeCal[m]), getbool(poly[m])))))
                           
            ''' v.insert(0,(int(xor(getbool(toBeCal[0]), getbool(poly[0])))))
            v.insert(1,(int(xor(getbool(toBeCal[1]), getbool(poly[1])))))
            v.insert(2,(int(xor(getbool(toBeCal[2]), getbool(poly[2])))))
            v.insert(3,(int(xor(getbool(toBeCal[3]), getbool(poly[3])))))'''
            
            
            if v[0] == 0:
                toBeCal = str(v[1])
                for m in range(orderOfGenerator - 2):
                    toBeCal += str(v[m+2])
                toBeCal += message[t+orderOfGenerator]
                '''if v[1] == 0:
                    toBeCal = str(v[2])+str(v[3])+message[t+4]+message[t+5]
                    if v[2] == 0:
                        toBeCal = str(v[3])+ message[t+4]+message[t+5]+message[t+6]
                        if v[3] == 0:
                            toBeCal = message[t+4]+message[t+5]+message[t+6]+message[t+7]
                        
                '''
                
            
            
        else:
            tempToBeCal = toBeCal
            toBeCal = tempToBeCal[1]
            for m in range(orderOfGenerator - 2):
                    toBeCal += str(tempToBeCal[m+2])
            toBeCal += message[t+orderOfGenerator]
        print(toBeCal)    
        t+=1
        v=[]
    



    
    if int(toBeCal) > 0:
        root = tk.Tk()
        w = tk.Label(root, text="Message is wrong")
        w.pack()
        root.mainloop()
    elif int(toBeCal) == 0:
        root = tk.Tk()
        w = tk.Label(root, text="Message is correct")
        w.pack()
        #root.mainloop()
######################################################################################
def alt(bitnum, str1):
    str1 = list(str1)
    if str1[bitnum-1] == "0":
        str1[bitnum-1] = "1"
    elif str1[bitnum-1] == "1":
        str1[bitnum-1] = "0"
    str1 = ''.join(str1)    
    return str1    
######################################################################################        
'''filename = "message_generator.txt"
inputfile = open(filename, "r")
Input = inputfile.readlines()
message = Input[0]
poly = Input[1]'''
'''transmitted = gen(message, poly)
transmitted = alt(3, transmitted)
ver(transmitted, poly)'''
#############################################################################################
from tkinter import *
fields = ('Message', 'Polynomial','Alter Value')

def withoutalter (entries):
   
   message = entries['Message'].get()
   print("message", message)
   
   poly = entries['Polynomial'].get()
   print("Poly", poly)
   
   #alter = int(entries['Alter Value'].get())
   
   
   transmitted = gen(message, poly)
   ver(transmitted, poly)
   '''entries['Transmitted Message'].delete(0,END)
   entries['Transmitted Message'].insert(0, transmitted )
   entries['Transmitted Message'].set(transmitted)
   print("t" + transmitted)
   ''' 
def withalter(entries):
   message = entries['Message'].get()
   print("message", message)
   
   poly = entries['Polynomial'].get()
   print("Poly", poly)
   
   alter = int(entries['Alter Value'].get())
   
   
   transmitted = gen(message, poly)
   transmitted = alt(alter, transmitted)
   ver(transmitted, poly)

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Gen-Alt-Ver',
          command=(lambda e=ents: withalter(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Gen-Ver',
          command=(lambda e=ents: withoutalter(e)))
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()

