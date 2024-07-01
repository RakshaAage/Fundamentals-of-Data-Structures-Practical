/*A palindrome is a string of character that‘s the same forward and backward. Typically, punctuation, capitalization, 
and spaces are ignored. For example, “Poor Dan is in a droop” is a palindrome, as can be seen by examining the characters
“poor danisina droop” and observing that they are the same forward and backward. One way to check for a palindrome is to reverse
the characters in the string and then compare with them the original-in a palindrome, the sequence will be identical. Write C++ program with functions- 
a) To print original string followed by reversed string using stack 
b) To check whether given string is palindrome or not*/

//SE-B-1

#include<iostream>
#include<string.h>
//#define max 50
using namespace std;

class STACK
{
	private:
		char a[50];
		int top;	
	public:
		STACK()
		{
			top=-1;	
		}	
		void push(char);
		void reverse();	
		void convert(char[]);
		void palindrome();
};

void STACK::push(char c)     //increment the top n insert the element in the top index of the array 
{
	top++;      
	a[top] = c;
	a[top+1]='\0';
	cout<<endl<<c<<" is pushed on stack.";
}

void STACK::reverse()
{
	char str[50];
	cout<<"\nReverse string is : ";
	for(int i=top,j=0; i>=0; i--,j++)
	{
		cout<<a[i];     
		str[j]=a[i];    
	}	
	cout<<endl;
}

void STACK::convert(char str[])
{
	int j,k,len = strlen(str);
	for(j=0, k=0; j<len; j++)      ///ascii values A-Z=65-90 a-z=97-122
	{
		if( ( (int)str[j] >= 97 && (int)str[j] <=122 ) || ( (int)str[j] >= 65 && (int)str[j] <=90 ))
		{
			if( (int)str[j] <=90 )
			{
				str[k] = (char)( (int)str[j] + 32 );
			}else
			{
				str[k] = str[j];				
			}
			k++;			
		}
	}
	str[k]='\0';
	cout<<endl<<"Converted String : "<<str<<"\n";
}

void STACK::palindrome()
{	
	char str[50];
	int i,j;		
	for(i=top,j=0; i>=0; i--,j++)
	{
		str[j]=a[i];
	}
	str[j]='\0';
	if(strcmp(str,a) == 0)
		cout<<"\n\nString is palindrome.";
	else
		cout<<"\n\nString is not palindrome.";
}

int main()
{
	STACK stack;
	char str[50];
	int i=0;
	cout<<"\nEnter string to be reversed and check if it is palindrome or not : \n";
	cin.getline(str , 50);
	stack.convert(str);
	while(str[i] != '\0')
	{
		stack.push(str[i]);
		i++;
	}
	stack.palindrome();
	stack.reverse();
}

//pop --- decrement the top and automatically the topmost element gets deleted
//underflow -- when we try to delete element from empty stack  i.e if top = -1 delete operation cannot be performed
//overflow -- when we try to insert an element in a stack which is full i.e if top==(stackSize-1) insert operation cannot be performed

//algorithm
/*
1.create an empty stack
2.push all characters of string one by one to stack
3.pop all characters one by one from stack n put them in a new string(reversed)
4.compare new n original string
if equal- string is palindrome
if not equal - not palindrome
*/	