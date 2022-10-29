#logical operators
'''x=5
print(x>3and x<10)
x=100
y=0.65
print(x and y)
y=0
print(x and y)                                                      #and:-both value should be non-zero to be true
print(x or y)                                                       #or:- any one value should be non-zero to be true
print(not(x and y))'''                                              #not:- reverses the result
'''x=20
y=50
z=10
print(not(x and(y or z)))'''

#conditional statement
'''x=int(input("Enter the 10+2 marks:"))
y=int(input("Enter the entrance test marks:"))
if(x>=90 and y>=120):
    print("Eligible for admission")
else:
    print("You are not eligible for admission")'''

'''a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if(a==6 and b==6 and c!=6):
    print("True")
else:
    print("False")'''

'''x=input("Enter the 1st string:")
y=input("Enter the 2nd string:")
print(x in y)

x=["apple","kela"]
print("kela"in x)
print("banana" not in x )'''                                 #the values assigned to a variable is known as object.

'''x=20
print(id(x))
print(hex(id(x)))
y=20
print(id(y))
print(hex(id(y)))'''
'''

x=200
y=200
print(x is y)

x=1.1
y=1.1
print(hex(id(x)))
print(hex(id(y)))        '''                                     #-5 to 256 range identity is same...

'''a=int(input("Enter an integer value: "))
b=int(input("Enter an integer value: "))
print(a,"+",b,"* 5 =",a+b*5)
print(a,"+",b,"* 5 * 10 / 2 =",a+b*5*10/2)'''

a=float(input("Enter marks of subject 1:"))
b=float(input("Enter marks of subject 2:"))
c=float(input("Enter marks of 3rd subject:"))
d=float(input("Enter marks of 4th subject:"))
e=float(input("Enter marks of 5th subject:"))
s=a+b+c+d+e
t=(a+b+c+d+e)/5
print(s)
print(t)
if(t>=60):
    print("Cleared")
else:
    print("Rewrite the exam")