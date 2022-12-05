import os

def printOut(a,count,i):
    cwd = os.getcwd()
    output_folder=os.path.join(cwd,'OUTPUT')
    if os.path.isfile(output_folder+"\output"+str(i)+".txt"):         
        with open(output_folder+"\output"+str(i)+".txt","r") as f1:
            for line in f1:
                pass
            lastLine=line
        if lastLine=='YES' or lastLine=='NO':
            os.remove(output_folder+"\output"+str(i)+".txt")
    with open(output_folder+"\output"+str(i)+".txt","a") as f:        
        print(count,file=f)
        for prop in a:
            for liter in prop:
                if liter != prop[len(prop)-1]:
                    if liter<0:
                        print("-"+chr((-1)*liter)+" OR",end= " ",file=f)
                    else: print(chr(liter)+" OR",end=" ",file=f)
                else:
                    if liter<0:
                        print("-"+chr((-1)*liter),file=f)
                    else: print(chr(liter),file=f) 
def printBrackets(i):
    cwd = os.getcwd()
    output_folder=os.path.join(cwd,'OUTPUT')
    with open(output_folder+"\output"+str(i)+".txt","a") as f:
        print('{}',file=f)
def printResult(res,i):
    cwd = os.getcwd()
    output_folder=os.path.join(cwd,'OUTPUT')
    with open(output_folder+"\output"+str(i)+".txt","a") as f:
        if res==True: print('YES',file=f)
        else: print ('NO',file=f)

def sorting(a):
    return sorted(a, key=abs)
def read_input(file_name):
    f= open(file_name,"r")
    alpha=f.readline().strip('\n')
    liters=[] #list of literals of each prop
    negativeAlpha=[]
    char=0
    for char in range(len(alpha)):
        if alpha[char] >= 'A' and alpha[char] <= 'Z' and alpha[char-2:char+1]!='AND' and alpha[char-1:char+2]!='AND' and alpha[char:char+3]!='AND':
            if alpha[char-1]=='-':
                negativeAlpha.append(ord(alpha[char]))
            else:
                negativeAlpha.append((-1)*ord(alpha[char]))
    liters.append(negativeAlpha)
    n=f.readline().strip('\n')
    props=[] #list of props in file input
    for line in f:
        props.append(line.strip('\n'))
    f.close()
    k=0
    for k in range(len(props)):
        " ".join((props[k]).split())
        char = 0
        liter=[]
        for char in range(len(props[k])):
            if props[k][char] >= 'A' and props[k][char] <= 'Z' and props[k][char-1:char+1]!='OR' and props[k][char:char+2]!='OR':
                if props[k][char-1]=='-':
                    liter.append((-1)*ord(props[k][char]))
                else:
                    liter.append(ord(props[k][char]))
            char+=1
        liters.append(sorting(liter))
    return liters
def PL_RESOLUTION(liters,index):
    brackets=False
    check=True
    res=True # Conclusion
    compared=[[0 for x in range(1000)] for y in range(1000)] # == 1 if 2 props compared

    while(check==True):     
        count=0
        sublist=[]
        for i in range(len(liters)-1):
            for j in range(i+1,len(liters)):
                if compared[i][j]==0: # neu chua so sanh
                    compared[i][j]=1
                    tmp=[]
                    if len(liters[i])==1 and len(liters[j])==1:     # if 1 to 1 literal props
                        if liters[i][0] + liters[j][0]==0:
                            if brackets==False:
                                brackets=True # print brackets
                                count+=1
                                check=False
                            else: continue
                    else:
                        if len(liters[i])==1 or len(liters[j])==1:  # if 1 of props only 1 literal
                            if len(liters[i])==1:
                                    for liter in liters[j]:
                                        if liters[i][0]+ liter == 0:
                                            tmp.append(liter)
                                            tmp=list(set(liters[j])-set(tmp))
                                            tmp=sorting(tmp)
                                            if tmp not in liters and tmp not in sublist: # kiem tra neu da ton tai menh de trong list thi khong in ra
                                                sublist.append(tmp)
                                                count+=1
                                            else: tmp=[]
                            else:
                                for liter in liters[i]:
                                        if liters[j][0]+ liter == 0:
                                            tmp.append(liter)
                                            tmp=list(set(liters[i])-set(tmp))
                                            tmp=sorting(tmp)
                                            if tmp not in liters and tmp not in sublist:
                                                sublist.append(tmp)
                                                count+=1
                                            else: tmp=[]
                        else:                                       # if many to many literals props
                            dn=0                                    # so cap doi ngau
                            for liter1 in  liters[i]:
                                for liter2 in  liters[j]:
                                    if liter1 + liter2 ==0:
                                        tmp.append(liter1)
                                        tmp.append(liter2)
                                        tmp=list(set(liters[i]+liters[j])-set(tmp))
                                        tmp=sorting(tmp)
                                        dn+=1
                            if tmp not in liters and tmp not in sublist and dn==1:
                                sublist.append(tmp)
                                count+=1
                            else: tmp=[]            
                    #if len(tmp)>0: print(tmp)
                else: continue # da so sanh 2 props, tiep tuc
        #print sublist here
        
        printOut(sublist,count,index)
        if brackets==True: printBrackets(index)
        liters=liters+sublist # nhap vao danh sach props nhung~ props moi sau khi het vong lap, sau do duyet lai danh sach props nay

        if count==0: 
            check= False
            res= False             
    printResult(res,index)
def main():
    cwd = os.getcwd()
    input_folder=os.path.join(cwd,'INPUT')
    index=0 # index of file
    for input in os.listdir(input_folder):
        file_name=os.path.join(input_folder, input)
        liters=read_input(file_name)
        PL_RESOLUTION(liters,index)
        index+=1
    return

if __name__ == "__main__":
    main()
