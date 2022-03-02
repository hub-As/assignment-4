#q1
def tower_of_hanoi(n,int_rod,to,etc):       
   if(n==1):
      print("move disc",n,"from",int_rod,"to",to)      # base case mof moving one disc
   else:
      tower_of_hanoi(n-1,int_rod,etc,to)                  #breaking in smaller problem by moving n-1 disc
      print("move disc",n,"from",int_rod,"to",to)         # moving last disc              
      tower_of_hanoi(n-1,etc,to,int_rod)                  # moving remaining disc to rod where nth disc is
print(tower_of_hanoi(3,'A','c','B'))


#q2a
def f(n,a):                                  # recusive function to calculate element of nth row and a th column 
    if a==1 or a==n:
        return 1
    else:
        return f(n-1,a-1)+f(n-1,a)

    
st=""
b=int(input("enter number of rows"))          #asking for input
for i in range(1,b+1):                       # loop for number of rows
    for j in range(1,i+1):                    # loop for number of columns
        st=st+str(f(i,j))+" "                 #converting into string for spacing
    print(st.center(2*b))                     #centering the stringto form proper triangle
    st=""
 

#q2b
a=list([1])                           #making two list that will store the row to be calculated and a previous row
b=list ([1,1])                        # a store the row to be calculated b store the previous calculated row
c=int(input("enter number of rows "))            
print(a)
print(b)
for i in range(1,c-1):                  # looping till desired number of rows
    a=list([1])                         # defining new row with first element as 1
    for j in range(len(b)-1):           # loop for calculating next row
        z=b[j]+b[j+1]  
        a.append(z)
        
    a.append(1)                          # adding last element
    print(a)
    b=list(a)                            # making copy of list a and storin it in b



#q3
def q_r(a,b):                               #function for finding quotient and remainder
    return [int(a/b),int(a%b)]

a=int(input("enter first number(integer)- "))           # asking for input 
b=int(input("enter second number(non zero integer)- "))
q=q_r(a,b)[0]
r=q_r(a,b)[1]                                            #storing remainder and quotient
print("Quotient is ",q,"\nremainder is ",r)
#part a
print("is function calleable",callable(q_r))
print("is value calleable",callable(q))
#part b
if (a == 0):
    print("The First number Is Zero")
if (b == 0):
    print("The second number Is Zero")
if (q == 0):
    print("The Quotient Is Zero")
if (r == 0):
    print("The Remainder Is Zero")
if a!=0 and b!=0 and q!=0 and r!=0:
    print ("all values are non zero")
#part c
lst=list(q_r(a,b).append([4,5,6]))
print("values greater than 4")

for i in lst:
    if i<=4:
        lst.remove(i)
#part d
st=set(lst)
print(st)
#part e
f_st=frozenset(st)
print(f_st)
#part f
print("maximum value is ",max(f_st))
print("its hash value is ",hash(max(f_st))



#q4
class Student:
  def __init__(self, name,roll_no):           #constuctor
    self.name = name
    self.roll_no = roll_no
  def __del__(self):
       print('Destructor called')
st1=Student("akshit",21103042)
print("Object Created...")
print(f"The Name Of The Student Is {st1.name} And SID Is {st1.roll_no}.")
del st1



#q5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

employee1.salary = 70000
print(f"The Updated Salary Of {employee1.name} Is {employee1.salary} ")   #updating salary

print("Record Of Viren Deleted!")
del employee3                                                    #deleting record



#q6
a=input("enter George's word ")
b=input("enter Barbie's word ")
a1=list(a.lower())
b1=list(b.lower())
a1.sort()
b1.sort()
if a!=b and a1==b1:
    m=input("is Barbie's word meaningful(Y/N) ")
    if m=='Y' or m=='y':
        print("their friendship is true")
else:
    print ( "their friendship is fake")
  
   
