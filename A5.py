'''
Write a Python program to store first year percentage of
students in array. Write function for sorting array of floating point
numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.
'''

marks=[]
n=int(input("Enter the no. of students :"))
for k in range(0,n):
    ele=float(input("Enter the percentage :"))
    marks.append(ele)

print("List of Percentage Before Sorting",marks)

def SelectionSort(marks,n):
    min_pos=0
    for i in range(0,n):
        min_pos=i
        for j in range(i+1,n):
            if marks[j]<marks[min_pos]:
                min_pos=j
                temp1=marks[i]
                marks[i]=marks[min_pos]
                marks[min_pos]=temp1
    


def BubbleSort(marks,n):
    for i in range(0,n):
        for j in range(0,n-1):
            if(marks[j]>marks[j+1]):
                temp=marks[j]
                marks[j]=marks[j+1]
                marks[j+1]=temp

print("Sorting using Selection Sort :")
SelectionSort(marks, n)
print(marks)
print("Sorting using Bubble Sort :")
BubbleSort(marks,n)
print(marks)
