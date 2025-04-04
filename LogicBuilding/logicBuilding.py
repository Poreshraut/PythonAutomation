'''8. How to swap first and last elements in the list'''
'''7. How to find the length of the list?'''
'''4. Print Fibonacci series.'''
'''3. How to find factorial of a number'''
'''2. How to check number is prime or not.'''
"""1. Write a program to swap two numbers."""
'''9. How to swap any two elements in the list?'''
'''10.How to remove the Nth occurrence of a given word list?'''
'''11. How to search an element in the list?'''
'''12. How to clear the list? --> 4 approaches'''
'''13. How to reverse a list? --> 2 approaches'''
'''14. How to clone or copy a list? --> 4 approaches'''
'''15.How to count occurrences of an element in a list? --> 2 approaches'''
'''16. Find the sum of the elements in list -- 2 approaches'''
'''17. How to multiply all the numbers in the list?'''
'''18. How to find the smallest and largest numbers on the list? --> 2 approaches'''
'''19. How to find the second largest number in a list?'''
'''20. How to check string is palindrome or not?'''
'''21. How to reverse words in a string?'''
'''22. How to find a substring in a string?'''
'''22. How to find a substring in a string?'''
'''23. How to find the length of a string? --> 2 approaches'''
'''24. How to check if the string contains any special character?'''
'''https://urlregex.com/''' ## get regular expression from this site 
'''25. Check for URL in a string'''
'''26. Remove odd number from the given list'''
'''27. Remove even number from the given list'''


# ----------------------------------------------------------------------------------------------------------------------

'''26. Remove odd number from the given list'''

# alist=[7,3,2,4,7,9,8,4,5,2,9,5,3,0,5]
# newlist=[]

# for i in alist:
#     if i % 2 != 0:
#         newlist.append(i)
# print(newlist)

'''27. Remove even number from the given list'''

# alist=[7,3,2,4,7,9,8,4,5,2,9,5,3,0,5]
# newlist=[]

# for i in alist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)

'''# 8. How to swap first and last elements in the list'''

# Cricket_Players=['Ms Dhoni','Virat Kohli','Shikhar Dhawan','Rohit Sharma','Suresh Raina','Ravindra Jadeja','Ravichandran Ashwin','Bhuvneshwar Kumar','Mohammad Shami','Umesh Yadav','Bumrah']

# Cricket_Players[0],Cricket_Players[len(Cricket_Players)-1]=Cricket_Players[len(Cricket_Players)-1],Cricket_Players[0]

# print(Cricket_Players)
#--------------------------------------------------------------------------------------------------------------------

'''7. How to find the length of the list?'''    

# Cricket_Players=['Ms Dhoni','Virat Kohli','Shikhar Dhawan','Rohit Sharma','Suresh Raina','Ravindra Jadeja','Ravichandran Ashwin','Bhuvneshwar Kumar','Mohammad Shami','Umesh Yadav','Bumrah']

# temp=len(Cricket_Players)
# print(temp)

##-----------------------------------------------------------------------------------------------------------------------

'''4. Print Fibonacci series.'''

# Add1=0
# Add2=1
# Result=0
# Upto=int(input('Enter Number :'))

# while Upto>Result:
#     print(Result)
#     Add1=Add2
#     Add2=Result
#     Result=Add1+Add2



##---------------------------------------------------------------------------------------------------------------------------------

'''3. How to find factorial of a number'''
# Factorial of number is the product of all the positive integer less than and equal to that number

# Starting=1
# Ending=int(input('Enter Number :'))
# Fact=1

# while Starting<=Ending:
#     Fact=Fact*Ending
#     Ending-=1
# print(Fact)    
    
##--------------------------------------------------------------------------------------------------------------------------

'''2. How to check number is prime or not.'''

# Starting=1
# Ending=int(input('Enter Number :'))
# Factor=0

# while Ending>=Starting:      ## Pay alway attention Here
#     if Ending%Starting==0:
#         Factor=Factor+1
#     Starting+=1
    
  
    
# if Factor==2:
#     print('It is Prime Number')
# else:
#     print('It is not Prime Number')

##----------------------------------------------------------------------------------------------------------------------------

"""1. Write a program to swap two numbers."""

# a=1
# b=2

# a=a+b
# b=a-b
# a=a-b

# print('After swapping Number a =',a)
# print('After swapping Number b =',b)

# a=a*b
# b=a/b
# a=a/b

# print('After swapping Number a =',int(a))
# print('After swapping Number b =',int(b))


# a,b=b,a
# print('After swapping Number a =',a)
# print('After swapping Number b =',b)

# c=a
# a=b
# b=c
# print('After swapping Number a =',a)
# print('After swapping Number b =',b)

# a=a^b
# b=a^b
# a=a^b
# print('After swapping Number a =',a)
# print('After swapping Number b =',b)

##------------------------------------------------------------------------------------------------------------

# XOR swap
# Addition sub straction swap
# Multiplication division swap
# User input third variable swap
# Python style swap

# a=2
# b=3

# a=a^b
# b=a^b
# a=a^b

# print('a after swap',a)
# print('b after swap',b)


'''Addition substraction'''
# a=4
# b=8

# a=a+b
# b=a-b
# a=a-b

# print('a after swap',a)
# print('a after swapt',b)


# a=int(input('Enter first number :'))
# b=int(input('Enter second number :'))

# a=a+b
# b=a-b
# a=a-b

# print('a after swapping',a)
# print('b after swapping',b)


'''Multiplication division'''

# a=1
# b=2

# a=a*b
# b=a/b
# a=a/b

# print('a after swapping',a)
# print('b after swapping ',b)

# a=int(input('Enter first number :'))
# b=int(input('Enter second number :'))

# a=a*b
# b=a/b
# a=a/b

# print('a after swapping',a)
# print('b after swapping',b)

'''Python method'''

# a=int(input('Enter first number :'))
# b=int(input('Enter seconf number :'))

# a,b=b,a

# print('a after swapping',a)
# print('b after swapping',b)

'''Third variable'''

# a=int(input('Enter first number :'))
# b=int(input('Enter second Number :'))

# temp=a
# a=b
# b=temp


# print('a after swapping',a)
# print('b after swapping',b)

##----------------------------------------------------------------------------------------------------------------------------


'''# 9. How to swap any two elements in the list?'''


# Home=['Table','Fan','Tv','Curtains','Bed','Sofa']

# print('Before Swapping :',Home)
# # print(type(Home))

# a=int(input('Enter a Index : '))
# b=int(input('Enter Second Index :'))
 
# Home[a],Home[b]=Home[b],Home[a]

# print('After swapping :',Home)

#-----------------------------------------------------------------------------------------------------------------------

'''10.How to remove the Nth occurrence of a given word list?'''

# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas']
# print('Before removing Nth occurrance :',len(House))
# occurance=2
# word='Bed'
# count=0
# for e in  range(0,len(House)-1):
#     if House[e]==word:
#         count=count+1
#         if count==occurance:
#             print(House[e])
#             del House[e]
        
# print('After removing Nth occurrance :',len(House))

##---------------------------------------------------------------------------------------------------------------
##------------------------------------------------------------------------------------------------------------------------

'''11. How to search an element in the list?'''

# House=['Bed','Family','Bed','Fan','Kitchen','Family','Bed','Kitchen','Fridge','Fan','Gas'] # 12

# search='Gas'
# count=0

# for i in range(0,len(House)):
#     if House[i]==search:
#         count=count+1
#         position=i+1
#         break
# if count==1:
#     print('Element is located in Position :',position)
# else:
#     print('Element is not Available')       

##-----------------------------------------------------------------------------------------------------------------

'''12. How to clear the list?'''

# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas'] # 12
# print('Before clear :',House)
'''Approach1'''
# House=[]
# print('After clear :',House)
'''Approach2'''
# House.clear()
# print('After clear :',House)
'''Approach3'''
# House*=0
# print('After clear :',House)
'''Approach4'''
# del House[:]
# print('After clear :',House)

##--------------------------------------------------------------------------------------------------------------------

'''13. How to reverse a list?'''

# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas'] # 12

# print('Before Reverse :',House)
'''Approach1'''
# House.reverse()
# print('After Reverse :',House)
'''Approach2'''
# House=House[::-1]
# print('After Reverse :',House)

##----------------------------------------------------------------------------------------------------------------

'''14. How to clone or copy a list?'''

# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas'] # 12
# print('Original :',House)
'''Approach1'''
# House1=House.copy()
# print(House1)
# House1[0]='Curtains'
# print(House1)
# print('Later :',House)
'''Approach2 Slicing technique'''
# House2=House[:]
# print(House2)
# House2[1]='Program'
# print(House2)
# print(House)
'''Approach3 extend() method'''
# House3=[]
# House3.extend(House)
# House3[0]='Poresh'
# print(House3)
# print(House)
'''Approach4 list() method'''
# House4=list(House)
# House4[0]='Rama'
# print(House4)
# print(House)
'''Approach5 list comprehension(loop)'''
# House5=[i for i in House]
# House5[0]='Rockstar'
# print(House5)
# print(House)

##----------------------------------------------------------------------------------------------------------------

'''15.How to count occurrences of an element in a list?'''

# from itertools import count

'''Approach1 by Loop'''
# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas'] # 12
# word='ten'
# count=0

# for i in range(0,len(House)-1):
#     if House[i]==word:
#         count=count+1
        
# if count>0:
#     print('Occurance :',count,'times')       
# else:
#     print('Element Not Available')     


'''Approach2 by count mrthod'''
# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas'] 

# print(House.count('Bed'))
# print(House.count('Family'))

'''Approach3 by Counter'''
# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas'] 

# from collections import Counter

# dic=Counter(House)
# print(dic)

##--------------------------------------------------------------------------------------------------------------------------

'''16. Find the sum of the elements in list'''

'''Approach1 for count the number of elements in the list'''
# House=['Bed','Family','Bed','Fan','Kitchen','Gas','Family','Bed','Kitchen','Fridge','Fan','Gas'] 
# count=0
# for i in House:
#     count=count+1
# print(count)    
  
'''Approach2 by using loop'''
# num=[10,30,20]
# total=0
# for i in range(0,len(num)):
#     total=total+num[i]
# print(total)

'''Approach3 by sum()'''
# num=[10,30,20]
# total=sum(num)
# print(total)

'''Approach4 by Reduce'''
# from functools import reduce
# summ=reduce(lambda a,b:a+b,alist)
# print(summ)

##--------------------------------------------------------------------------------------------------------------

'''17. How to multiply all the numbers in the list?'''

'''Approach1 loop'''
# num=[1,2,3,4]
# mul=1
# for i in range(0,len(num)):
#     mul=mul*num[i]
# print(mul)

'''Approach2 Reduce'''
# from functools import reduce
# mul=reduce(lambda a,b:a*b,alist)
# print(mul)

##---------------------------------------------------------------------------------------------------------------------------------------------------------

'''18. How to find the smallest and largest numbers on the list?'''

'''Approach1 Using loop'''
# Num=[1,2,3,4,5,6,7,8,9,10]
# Smallest=Num[0]
# Largest=Num[0]
# for i in range(0,len(Num)):
#     if Smallest>Num[i]:
#         Smallest=Num[i]
#     if Largest<Num[i]:
#         Largest=Num[i]
# print('Smallest Num is :',Smallest)
# print('Largest Num is :',Largest)

'''Approach2 Using Sort the list in ascending order and print the first and the last element in the list'''
# Num=[6,1,2,7,4,10,5,8,9,3]
# Num.sort()
# print(len(Num)-1)
# print('Largest num is :',Num[9])
# print('Smallest Num is :',Num[0])

'''Approach3 Using min() and max()'''
# Num=[6,1,2,7,4,10,5,8,9,3]
# print('Smallest Num is :',min(Num))
# print('Largest Num is :',max(Num))

##---------------------------------------------------------------------------------------------------------------------

'''19. How to find the second largest number in a list?'''

'''Approach1 using sort()'''
# Num=[6,1,2,7,4,10,5,8,9,3]
# Num.sort(reverse=True)
# print('Second Largest Number is :',Num[1])

'''Approach2 remove.max() method by converting into set'''
# Num=[6,1,2,7,4,10,5,8,9,3]
# New_num=set(Num)
# print(New_num)
# print(max(New_num))
# New_num.remove(max(New_num))
# print(New_num)
# print('Second largest Number is :',max(New_num))

##-------------------------------------------------------------------------------------------------------------------------

'''20. How to check string is palindrome or not?'''

## Palindrome :- The string after reversing remains the name is called palindrome
#Example :- Madam = madaM

'''Appraoch1'''
# word=input('Enter a String :')
# Reve=word[::-1]
# if word[:]==Reve:
#     print('It is a palidrome string')
# else:
#     print('It is not palidome string')    

##---------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''21. How to reverse words in a string?'''

'''Approach1 using reverse indexing,split(),Join() method'''
# sentence='what is your name'
# slist=sentence.split(' ')
# reve=slist[::-1]
# result=' '.join(reve)
# print(result)

##---------------------------------------------------------------------------------------------------------------------------------

'''22. How to find a substring in a string?'''

'''Approach1 using find() method'''
# sentence='My name is Poresh'
# word='Poresh'
# result=sentence.find(word)
# print(result)

# if result==-1:
#     print('Word not found')
# else:
#     print('Word found')

##-------------------------------------------------------------------------------------------------------------------

'''23. How to find the length of a string?'''

'''Approach1 Using len() function'''
# sentence='What is your Name ?'
# lenght=len(sentence)
# print(lenght)

'''Approach2 Using for loop'''
# sentence='What is your Name ?'
# count=0
# for i in sentence:
#     count = count+1
# print(count)

'''Approach3 Using while loop slicing'''
# sentence='What is your Name ?'
# count=0
# # while sentence[count:]:
# #     count=count+1
# # print(count)   

# print(sentence[count:])
# print(sentence[18:])

'''Approach4 Using join and count'''
# sentence='welcme'
# print(len(sentence))
# random='o'
# ass=random.join(sentence)
# print(ass)
# print(ass.count('o')+1)

##----------------------------------------------------------------------------------------------------------------

'''24. How to check if the string contains any special character?'''

# sentence='My@ name# is$ Poresh&'
# sentence1='what is your name'
# import re 
# regex=re.compile('[!@#$%^&*():|?><+_)(]')
# if regex.search(sentence1)==None:
#     print('Special character is not present')
# else:
#     print('Special character is present')

##---------------------------------------------------------------------------------------------------------------------------
'''https://urlregex.com/''' ## get regular expression from this site 
'''25. Check for URL in a string'''
# Reregular expression :- http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

# sentence='Google:https://www.google.com/ and facebook:https://www.facebook.com/'
# import re 
# url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',sentence)
# print(url)

##--------------------------------------------------------------------------------------------------------------------------------------------------------
