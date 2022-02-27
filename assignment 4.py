#q1
def tower_of_hanoi(n,int_rod,to,etc):
   if(n==1):
      print("move disc",n,"from",int_rod,"to",to)
   else:
      tower_of_hanoi(n-1,int_rod,etc,to)
      print("move disc",n,"from",int_rod,"to",to)
      tower_of_hanoi(n-1,etc,to,int_rod)
print(tower_of_hanoi(3,'A','c','B'))


#q2a
def f(n,a):
    if a==1 or a==n:
        return 1
    else:
        return f(n-1,a-1)+f(n-1,a)

    
st=""
b=int(input("enter number of rows"))
for i in range(1,b+1):
    for j in range(1,i+1):
        st=st+str(f(i,j))+" "
    print(st.center(2*b))
    st=""
 

#q2b
a=list([1])
b=list ([1,1])
c=int(input("enter number of rows "))
print(a)
print(b)
for i in range(1,c-1):
    a=list([1])
    for j in range(len(b)-1):
        z=b[j]+b[j+1]
        a.append(z)
        
    a.append(1)
    print(a)
    b=list(a)



#q3
def q_r(a,b):
    return [int(a/b),int(a%b)]

a=int(input("enter first number(integer)- "))
b=int(input("enter second number(integer)- "))
q=q_r(a,b)[0]
r=q_r(a,b)[1]
print("Quotient is ",q,"\nremainder is ",r)
print("is function calleable",callable(q_r))
print("is value calleable",callable(q))

if (a == 0):
    print("The First Is Zero")
if (b == 0):
    print("The second Is Zero")
if (q == 0):
    print("The Quotient Is Zero")
if (r == 0):
    print("The Remainder Is Zero")
if a!=0 and b!=0 and q!=0 and r!=0:
    print ("all values are non zero")

print("values greater than 4")
lst=[q+4,q+5,q+6,r+4,r+5,r+6]
for i in lst:
    if i<=4:
        lst.remove(i)
st=set(lst)
print(st)
f_st=frozenset(st)
print(f_st)
print("maximum value is ",max(f_st))
print("its hash value is ",hash(f_st))



#q4
class Student:
  def __init__(self, name,roll_no):
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
print(f"The Updated Salary Of {employee1.name} Is {employee1.salary} ")

print("Record Of Viren Deleted!")
del employee3



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
  
   
