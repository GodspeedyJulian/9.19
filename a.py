#Character as string
# NewText as string
Character=str(input('input a character:'))
NewText=''
FileHandle=open('qbdata.txt','r')
FileHandle2=open('NewData.txt','w')
Line=FileHandle.readline()
while len(Line)>0:
    for i in range(len(Line)):
        if Line[i]!=' ':
            NewText+=Line[i]
        else:
            NewText+=Character
    FileHandle2.write(NewText)
    LineOfText=FileHandle.readline()
FileHandle.close()
FileHandle2.close()

