'''Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. Write functions to compute following:
a.The average score of class
b.Highest score and lowest score of class
c.Count of students who were absent for the test
d.Display mark with highest frequency'''
#SE-B-1

n=int (input("Enter the number of students: "))  
    
marks=[]
print("Enter the marks of student...(Enter -1 for absent students)")
for i in range(n):
    m=int(input())
    marks.append(m)
        
print("The list of students score is: ", marks)
    
def avg_score():
    total=0
    for i in range (n):
        if (marks[i]!= -1):
            total=total+ marks[i]
        
    print("Total marks are: ",total)
    print("Average marks are: ",total/len(marks))
    
def max_min():
    
    max=marks[0]
    for i in range(n):
        if(marks!=-1):
            if(marks[i]>max):
                max=marks[i]
    print("Maximum marks obtained are: ", max)

    mini=max
    for i in range (n):
        if (marks[i] != -1):
            if(marks[i]<mini):
                mini=marks[i]
    print("Minimum marks obtained are: ", mini)
        
        
def absent():
    cnt=0
    for i in range (n):
        if(marks[i]==-1):
            cnt=cnt+1
            
    print("The number of absent students are: ",cnt)
    
def high_freq():
    highf=0
    highf_marks=0
    
    for i in marks:
        cur_freq= marks.count(i)
        if(marks!=-1):
            if(cur_freq> highf):
                highf=cur_freq
                highf_marks=i
            
    print("Marks with highest frequency is: ", highf_marks)

ch=0
while(ch!=5):

    print("Enter your choice: ")
    print("1. Average marks ")
    print("2. Maximum and Minimum marks")
    print("3. Number of absent students ")
    print("4. highest frequency marks")
    print("5. Exit") 
    ch=int(input('choice=' ))
    
    if(ch==1):
       avg_score() 
       
    elif(ch==2):
        max_min()
    
    elif(ch==3):
        absent() 
        
    elif(ch==4):
         high_freq()
         
    elif(ch==5):
        break