'''Write a Python program to compute following computation on matrix:
a)  Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix'''
#SE-B-1

r1=int(input("Enter the number of rows for 1st matrix: "))
c1=int(input("Enter the number of columns for 1st matrix: "))

matrix1=[]
print("Enter the elements row-wise: ")
for i in range(r1):
    m1=[]
    for j in range(c1):
        ele=int(input())
        m1.append(ele)
    matrix1.append(m1)
    
for i in range (r1):
    print("\n")
    for j in range (c1):
        print(matrix1[i][j] , end="  ")
    

r2=int(input("\nEnter the number of rows for 2nd matrix: "))
c2=int(input("Enter the number of columns for 2nd matrix: "))


matrix2=[]
print("Enter the elements row-wise: ")
for i in range(r2):
    m2=[]
    for j in range(c2):
        ele=int(input())
        m2.append(ele)
    matrix2.append(m2)
    
for i in range (r2):
    print("\n")
    for j in range (c2):
        print(matrix2[i][j] , end="  ")
    
    
def add():
    if(r1==r2 and c1==c2):
        add=[]
        for i in range (r1):
            r=[]
            for j in range(c1):
                a=matrix1[i][j] + matrix2[i][j]
                r.append(a)
            add.append(r)
            
        for i in range (r1):
            print("\n")
            for j in range (c1):
                print(add[i][j] , end="  ")
    
    else:
        print("\nAddition cannot be performed")
            
def sub():
    
    if(r1==r2 and c1==c2):
        sub=[]
        for i in range (r1):
            r=[]
            for j in range(c1):
                a=matrix1[i][j] - matrix2[i][j]
                r.append(a)
            sub.append(r)
            
        for i in range (r1):
            print("\n")
            for j in range (c1):
                print(sub[i][j] , end="  ")
                
    else:
        print("\nSubtraction cannot be performed")
            
            
def multi(row,col):
    C=[[0 for i in range (col)] for j in range (row)]
    
    for i in range(row):
        for j in range(col):
            C[i][j]=0
            for k in range(row):
                C[i][j]+=matrix1[i][k]*matrix2[k][j]
    
    for i in range(r1):
        print("\n")
        for j in range(c1):
            print(C[i][j],end=" ")
            
def transpose(r1,c1):
    trans=[]
    
    for i in range (r1):
        r=[]
        for j in range(c1):
            r.append(0)
        trans.append(r)
        
    for i in range (r1):
        for j in range(c1):
            trans[i][j]=matrix2[j][i]
            
    for i in range (r1):
        print("\n")
        for j in range (c1):
            print(trans[i][j] , end="  ")
            
            
ch=0
while(ch!=5):

    print("\n\nEnter your choice: ")
    print("1. Addition \t2. Subtraction \n3. Multiplication \t4. Transpose \n5. Exit")
    ch=int(input("Choice:"))
    
    if(ch==1):
       add()       
    elif(ch==2):
        sub()
    elif(ch==3):
        multi(2,2)    
    elif(ch==4):
        print("Transpose of 1st matrix is: ")
        transpose(r1,c1)
        print("Transpose of 2nd matrix is: ")
        transpose(r2,c2)
    elif(ch==5):
        break