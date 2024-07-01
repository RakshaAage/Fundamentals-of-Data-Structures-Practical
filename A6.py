'''Write a Python program to store second year percentage of students in array.
Write function for sorting array of floating point numbers in ascending order using
Insertion sort
Shell Sort and display top five scores'''
#SE-B-1

def insertion_sort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while(j>=0 and key<array[j]):
            array[j+1]=array[j]
            j-=1
        array[j+1]=key       

def shell_sort():
    gap=n//2
    while(gap>0):
        for i in range(gap, n ):
            temp=data[i]
            j=i
            while(j>=gap and data[j-gap]>temp):
                data[j]=data[j-gap]
                j-=gap
            data[j]=temp    
        gap//=2     
    
def top_score(n):
    if(n >= 5) :
        print("\nTop Five Scores : ")
        for i in range(n-1,n-6,-1) :
            print(data[i],end=" , ")
    else :
        print("\nTop Scorers : ")
        for i in range(n-1,-1,-1) :
            print(data[i],end=" , ")   
        
data=[]
n=int(input("Enter the total number of the students: "))
print("Enter the percentage of second year students")
for i in range(n):
    print("Student ",i+1," = ")
    m=float(input())
    data.append(m)
    
print("Array of SE marks: ")    
for i in range(n):
    print(data[i],end=" , ") 
insertion_sort(data)
print("\n---Array after sorting using Insertion sort----")
for i in range(n):
    print(data[i],end=" , ")    
shell_sort()
print("\n---Array after sorting using Shell sort----")
for i in range(n):
    print(data[i],end=" , ")   
top_score(n)   