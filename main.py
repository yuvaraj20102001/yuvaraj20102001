#FLAMES GAME
def common_character(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if(l1[i]==l2[j]):
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l3=l1+["*"]+l2
                return [l3,True]
    l3=l1+["*"]+l2
    return [l3,False]

print("\t::::::FLAMES GAME:::::")
print("\n")
name1=input("ENTER YOUR NAME::")
name2=input("ENTER SECOND NAME TO PERFORM FLAMES::")
print("\n")
name1=name1.upper()
name1.replace(" ","")
name1_list=list(name1)
name2=name2.upper()
name2.replace(" ","")
name2_list=list(name2)
print(name1_list,name2_list)

flag=True

while flag:
    l=common_character(name1_list,name2_list)
    newlist=l[0]
    flag=l[1]
    sindex=newlist.index("*")
    name1_list=newlist[:sindex]
    name2_list=newlist[sindex+1:]
    print(name1_list,name2_list)
print("\n")
count=len(name1_list)+len(name2_list)

res=["FRIENDS","LOVER","AFFECTION","MARRIAGE","ENEMY","SIBLING"]
for i in res:
        print(i[0],"::",i)

while len(res)>1:
    split=(count%len(res)-1)
    if(split>=0):
        r=res[split+1 :]
        l=res[:split]
        res=r+l
    else:
        res=res[:len(res)-1]
print("\n")    
print("RELATIONSHIP FROM FLAMES::",res[0])