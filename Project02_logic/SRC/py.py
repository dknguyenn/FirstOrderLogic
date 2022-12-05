import os
y=[[-65], [-65, 66], [-67, 66], [65, 67, -66], [-66]]
tmp=[-65]

#print(type(x) is list)
# tmp=[]
# s='{}'
# tmp.append(s[0])
# print(tmp)

# x=[10,20]
# z=[-20,30]
# #tmp=[20,-20]
# #tmp = list(set(x)-set(z))
# def sorting(a):
#     b=[]
#     for i in a:
#         b.append(sorted(i, key=abs))
#     return b


# def printOut(a,count):
#     with open("output.txt","w") as f:
#         print(count,file=f)
#         for prop in a:
#             for liter in prop:
#                 if liter != prop[len(prop)-1]:
#                     if liter<0:
#                         print("-"+chr((-1)*liter)+" OR",end= " ",file=f)
#                     else: print(chr(liter)+" OR",end=" ",file=f)
#                 else:
#                     if liter<0:
#                         print("-"+chr((-1)*liter),file=f)
#                     else: print(chr(liter),file=f) 
# printOut(y,2)
alpha='-A'
liters=[] #list of literals of each prop
char=0
negaAlpha=[]
for char in range(len(alpha)):
    if alpha[char] >= 'A' and alpha[char] <= 'Z' and alpha[char-2:char+1]!='AND' and alpha[char-1:char+2]!='AND' and alpha[char:char+3]!='AND':
        if alpha[char-1]=='-':
            negaAlpha.append(ord(alpha[char]))
        else:
            negaAlpha.append((-1)*ord(alpha[char]))
liters.append(negaAlpha)

#print(liters)
cwd = os.getcwd()
input_folder=os.path.join(cwd,'SRC')
input_folder=os.path.join(cwd,'INPUT')
print(input_folder)

cwd = os.getcwd()
output_folder=os.path.join(cwd,'SRC\OUTPUT')
with open(output_folder+"\output"+"0"+".txt","a") as f:
    print('test',file=f)

# y=sorting(y)
# print(y)