#Code as string
#Found as Boolean

Code=input('Please input the code for the student: ')
FileHandle=open('qbdata.txt','r')
for Line in FileHandle.readlines():
    
    Found=False
    for i in Line:
        if Line[:4]==Code:
            print("Student found ")
            Found=True
            break
if Found==False:
    print('Student not found')
