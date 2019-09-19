a=input("input a name you want to remove: ")
FileHandle=open("qbdata.txt","r")
NewList=[]
for Line in FileHandle.readlines():
    for i in range(len(Line)):
        if Line[i]==" ":
            Space+=1
            if Space==2:
                Name = Line[:i]
                break
        if Name!=a:
            NewList.append(Line)
FileHandle.close()
FileHandle=open("Newqbdata2.txt","w")
for i in range (len(NewList)):
    FileHandle.write(NewList[i])
FileHandle.close()
