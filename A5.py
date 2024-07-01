'''Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
Selection Sort
Bubble sort and display top five scores.'''
#SE-B-1

def SelectionSort(data,n):
    temp=0
    for i in range(n):
        for j in range(i+1,n):
            if(data[i]<data[j]):
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
            j+=1
        i+=1
    print("***Sorting using Selection sort***")
    print(data)
    print("Top five scores are : ")
    for i in range(0,5):
        print(data[i])

#sorting this data using bubble sort.
def bubbleSort(data,n):
    for i in range(n-1):
        for  j in range(n-i-1):
            if(data[j]>data[j+1]):
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    print("***Sorting using Bubble sort***")
    print(data)
  

ele=int(input("Enter number of students:"))
if(ele>5):
    print("Enter percentage of first year students")
    data=[]
    for i in range(ele):
        print("Student",i+1,"=")
        stud=float(input())
        data.append(stud)
    n=len(data)
    
    bubbleSort(data,n)
    
    SelectionSort(data,n)